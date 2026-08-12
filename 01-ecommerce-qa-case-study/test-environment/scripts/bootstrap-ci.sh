#!/usr/bin/env bash

set -Eeuo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
environment_dir="$(cd -- "${script_dir}/.." && pwd)"
compose_project="${COMPOSE_PROJECT_NAME:-nopcommerce-ci}"
store_port="${NOPCOMMERCE_PORT:-8080}"
base_url="http://localhost:${store_port}"
work_dir="$(mktemp -d)"

: "${MSSQL_SA_PASSWORD:?MSSQL_SA_PASSWORD must be set}"
: "${NOP_ADMIN_EMAIL:?NOP_ADMIN_EMAIL must be set}"
: "${NOP_ADMIN_PASSWORD:?NOP_ADMIN_PASSWORD must be set}"

compose() {
  docker compose \
    --project-directory "${environment_dir}" \
    --project-name "${compose_project}" \
    --file "${environment_dir}/docker-compose.yml" \
    "$@"
}

diagnose() {
  echo "::group::Docker Compose status"
  compose ps || true
  echo "::endgroup::"
  echo "::group::Docker Compose logs"
  compose logs --no-color --tail 300 || true
  echo "::endgroup::"
}

cleanup() {
  local status=$?
  trap - EXIT
  rm -rf "${work_dir}"
  if (( status != 0 )); then
    diagnose
  fi
  exit "${status}"
}
trap cleanup EXIT

wait_for_container_health() {
  local service="$1"
  local attempts="$2"
  local container_id health

  for ((attempt = 1; attempt <= attempts; attempt++)); do
    container_id="$(compose ps -q "${service}")"
    if [[ -n "${container_id}" ]]; then
      health="$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}{{.State.Status}}{{end}}' "${container_id}")"
      if [[ "${health}" == "healthy" ]]; then
        echo "${service} container is healthy."
        return 0
      fi
    fi
    sleep 5
  done

  echo "Timed out waiting for ${service} container health." >&2
  return 1
}

wait_for_install_page() {
  local attempts="$1"
  local status

  for ((attempt = 1; attempt <= attempts; attempt++)); do
    status="$(curl --silent --show-error --output "${work_dir}/install.html" --write-out '%{http_code}' --max-time 15 "${base_url}/install" || true)"
    if [[ "${status}" == "200" ]] && grep --quiet 'id="installation-form"' "${work_dir}/install.html"; then
      echo "nopCommerce installation page is reachable."
      return 0
    fi
    sleep 5
  done

  echo "Timed out waiting for the nopCommerce installation page." >&2
  return 1
}

wait_for_storefront() {
  local attempts="$1"
  local status

  for ((attempt = 1; attempt <= attempts; attempt++)); do
    status="$(curl --silent --show-error --output "${work_dir}/home.html" --write-out '%{http_code}' --max-time 15 "${base_url}/" || true)"
    if [[ "${status}" == "200" ]] \
      && ! grep --quiet 'nopCommerce installation' "${work_dir}/home.html" \
      && grep --quiet 'nopCommerce' "${work_dir}/home.html"; then
      echo "nopCommerce storefront is reachable."
      return 0
    fi
    sleep 5
  done

  echo "Timed out waiting for the installed nopCommerce storefront." >&2
  return 1
}

verify_sample_catalog() {
  curl --fail --silent --show-error --max-time 20 \
    --output "${work_dir}/simple-product.html" \
    "${base_url}/digital-storm-vanquish-custom-performance-pc"
  grep --quiet 'Digital Storm VANQUISH Custom Performance PC' "${work_dir}/simple-product.html"

  curl --fail --silent --show-error --max-time 20 \
    --output "${work_dir}/configurable-product.html" \
    "${base_url}/build-your-own-computer"
  grep --quiet 'Build your own computer' "${work_dir}/configurable-product.html"

  curl --fail --silent --show-error --max-time 20 \
    --output "${work_dir}/search.html" \
    "${base_url}/search?q=computer"
  grep --quiet 'Build your own computer' "${work_dir}/search.html"

  curl --fail --silent --show-error --max-time 20 \
    --output "${work_dir}/manufacturer-filter.html" \
    "${base_url}/shoes?ms=3"
  grep --quiet 'Nike' "${work_dir}/manufacturer-filter.html"
  echo "Required sample catalog targets are available."
}

echo "Starting pinned nopCommerce and SQL Server services."
compose up --detach database storefront
wait_for_container_health database 36
wait_for_container_health storefront 36
wait_for_install_page 36

curl --silent --show-error \
  --cookie-jar "${work_dir}/cookies.txt" \
  --output "${work_dir}/install.html" \
  --max-time 30 \
  "${base_url}/install"

verification_token="$(
  grep --only-matching 'name="__RequestVerificationToken" type="hidden" value="[^"]*"' "${work_dir}/install.html" \
    | head -n 1 \
    | sed 's/.*value="\([^"]*\)"/\1/'
)"

if [[ -z "${verification_token}" ]]; then
  echo "Installation antiforgery token was not found." >&2
  exit 1
fi

echo "Installing nopCommerce with ephemeral credentials and sample data."
curl --fail-with-body --silent --show-error \
  --cookie "${work_dir}/cookies.txt" \
  --cookie-jar "${work_dir}/cookies.txt" \
  --output "${work_dir}/install-response.html" \
  --max-time 600 \
  --request POST \
  --data-urlencode "__RequestVerificationToken=${verification_token}" \
  --data-urlencode "AdminEmail=${NOP_ADMIN_EMAIL}" \
  --data-urlencode "AdminPassword=${NOP_ADMIN_PASSWORD}" \
  --data-urlencode "ConfirmPassword=${NOP_ADMIN_PASSWORD}" \
  --data-urlencode "Country=US-en-US" \
  --data-urlencode "InstallSampleData=true" \
  --data-urlencode "SubscribeNewsletters=false" \
  --data-urlencode "DataProvider=1" \
  --data-urlencode "CreateDatabaseIfNotExists=true" \
  --data-urlencode "ConnectionStringRaw=false" \
  --data-urlencode "ServerName=database" \
  --data-urlencode "DatabaseName=nopcommerce" \
  --data-urlencode "IntegratedSecurity=false" \
  --data-urlencode "Username=sa" \
  --data-urlencode "Password=${MSSQL_SA_PASSWORD}" \
  --data-urlencode "UseCustomCollation=false" \
  "${base_url}/install"

if ! compose exec --no-TTY storefront sh -c \
  'grep -Eq '"'"'"ConnectionString"[[:space:]]*:[[:space:]]*".+"'"'"' /app/App_Data/appsettings.json && grep -q '"'"'"DataProvider": "sqlserver"'"'"' /app/App_Data/appsettings.json'; then
  echo "nopCommerce did not persist a valid SQL Server installation configuration." >&2
  exit 1
fi

echo "Restarting storefront to load the generated installation configuration."
compose restart storefront
wait_for_container_health storefront 36
wait_for_storefront 36
verify_sample_catalog

echo "Controlled nopCommerce environment bootstrap completed successfully."
