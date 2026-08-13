# Controlled nopCommerce Test Environment

This Docker Compose environment provides an isolated nopCommerce storefront and database for the Cypress portfolio suite. It uses pinned images for reproducibility:

- nopCommerce `4.90.6`: `nopcommerceteam/nopcommerce:4.90.6`
- Microsoft SQL Server 2022 CU20 Express: `mcr.microsoft.com/mssql/server:2022-CU20-ubuntu-22.04`

The environment is for local QA development only. It is not production-hardened and must not contain real credentials or customer data.

## Prerequisites

- Docker Desktop with Linux containers
- Docker Compose
- Ports `8080` (or the configured alternative) available locally

## Configure

Copy `.env.example` to `.env`, then replace the local-development-only password values. `.env` is ignored by Git.

```powershell
Copy-Item .env.example .env
```

## Start

```powershell
docker compose up -d
docker compose ps
```

Open `http://localhost:8080`. On the first start, complete the nopCommerce installer with:

- Admin email/password: values from local `.env`
- Create sample data: enabled
- Database: Microsoft SQL Server
- Server: `database`
- Database name: `nopcommerce`
- SQL username: `sa`
- SQL password: `MSSQL_SA_PASSWORD` from local `.env`
- Create database if it does not exist: enabled

The database and nopCommerce `App_Data` use named volumes, so the installed store persists across container restarts.

After the first installation completes, restart only the storefront so it reloads the generated `App_Data/appsettings.json`:

```powershell
docker compose restart storefront
```

## Cypress

The automation suite defaults to `http://localhost:8080` after the controlled environment is initialized:

```powershell
Set-Location ..\automation
npm test
```

Override the target without duplicating the suite:

```powershell
$env:CYPRESS_BASE_URL = "https://demo.nopcommerce.com"
npm test
```

The public demo is an optional smoke target and is known to return HTTP 403 to Cypress. Do not add anti-bot bypass logic.

## Automated CI Bootstrap

`scripts/bootstrap-ci.sh` provisions a fresh Compose project without browser interaction. It:

1. starts the pinned SQL Server and nopCommerce services;
2. waits for container health and the installation endpoint;
3. submits the nopCommerce installer over HTTP with ephemeral credentials and sample data enabled;
4. verifies the generated SQL Server configuration and restarts the storefront;
5. waits for the installed homepage and checks the required sample catalog targets.

All readiness loops are bounded. On failure the script prints Compose status and recent logs. CI credentials are generated per GitHub Actions run and are never committed.

The GitHub-hosted workflow is `.github/workflows/cypress.yml` on `ubuntu-24.04`. It creates a fresh environment, runs the TypeScript check, executes the same ten Cypress tests through `cypress-io/github-action@v7`, uploads failure screenshots when present, and removes containers and volumes afterward.

## Reset

To stop containers while retaining installed data:

```powershell
docker compose down
```

To intentionally reset the controlled store and database, remove the named volumes:

```powershell
docker compose down --volumes
```

The volume-reset command permanently deletes only this Compose project's local nopCommerce data.

## Compatibility Mapping

| Automation Need | Public Demo Target | Local Target | Compatible |
|---|---|---|---|
| Simple product | Digital Storm VANQUISH Custom Performance PC | Digital Storm VANQUISH Custom Performance PC | YES |
| Configurable product | Build your own computer | Build your own computer, with the same Processor/RAM/HDD/OS/Software options used by the suite | YES |
| Search keyword | computer | `computer` returns the sample computer catalog | YES |
| Manufacturer filter | Shoes / Nike | Shoes category with Nike manufacturer (`ms=3`) | YES |

The 4.90.6 sample catalog matched all fixture data used by the ten tests, so no fixture substitutions were required. The local cart quantity control recalculates after the quantity field loses focus; the Cypress test preserves the same quantity/subtotal/total assertions without relying on an update-button selector.

## Verified Local Result

- Local URL: `http://localhost:8080`
- nopCommerce: `4.90.6`
- Database: Microsoft SQL Server 2022 CU20 Express
- Sample data: enabled
- Cypress: 10 executed, 10 passed, 0 failed
- Full-run duration: 21 seconds

A separate fresh-volume validation of the non-interactive bootstrap also completed successfully and produced 10/10 Cypress passes. GitHub Actions then reproduced the result with 10 executed, 10 passed, and 0 failed on the [verified GitHub Actions run](https://github.com/ndo-fer/software-qa-portfolio/actions/runs/31572314690).
