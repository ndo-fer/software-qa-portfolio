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
