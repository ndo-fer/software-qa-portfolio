# nopCommerce Cypress Regression Suite

This TypeScript Cypress suite automates ten regression checks selected from the approved e-commerce test baseline. The public nopCommerce demo blocks Cypress with HTTP 403, so the suite runs against the controlled environment described below.

## Why These Tests

The selected checks cover negative authentication behavior, anonymous access control, core product discovery, product-detail business rules, cart calculations, and configuration identity. They run without account creation, stored credentials, checkout, or persistent test data.

## Traceability

| Cypress Test | Detailed TC | Scenario | Requirement | Coverage |
|---|---|---|---|---|
| Reject invalid login and clear credentials | TC-AUTH-003 | SCN-AUTH-004, SCN-AUTH-005, SCN-AUTH-006 | REQ-AUTH-004 | Automated |
| Redirect anonymous protected-page access | TC-AUTH-004 | SCN-AUTH-007 | REQ-AUTH-005 | Automated |
| Search with known product-title keyword | TC-DISC-002 | SCN-DISC-002 | REQ-DISC-002 | Automated |
| Display zero-result search state | TC-DISC-003 | SCN-DISC-003 | REQ-DISC-003 | Automated |
| Filter shoes by Nike manufacturer | TC-DISC-005 | SCN-DISC-005 | REQ-DISC-005 | Automated |
| Display simple-product purchase information | TC-PDP-001 | SCN-PDP-001, SCN-PDP-002 | REQ-PDP-001 | Automated |
| Block incomplete required configuration | TC-PDP-002 | SCN-PDP-003 | REQ-PDP-002 | Automated |
| Recalculate cart totals for quantity update | TC-CART-001 | SCN-CART-001 | REQ-CART-001 | Automated |
| Merge identical configured products | TC-CART-005 | SCN-CART-009 | REQ-CART-005 | Automated |
| Separate different product configurations | TC-CART-006 | SCN-CART-010 | REQ-CART-006 | Automated |

## Test Isolation

Cypress test isolation is enabled. Every test invokes a state-establishment helper that clears browser storage, starts an anonymous session, and confirms an empty cart. Cart tests create all required items inside the current test. Helpers do not share or preserve state between tests, and no test depends on execution order.

## Coverage Outside This Cypress Suite

Registration, authenticated-session flows, advanced search, sorting and layout-state preservation, cart removal and mini-cart synchronization, guest checkout, payment-method presentation, order completion, post-order cart reset, exploratory testing, and accessibility/usability review are outside this first Cypress suite. These areas require broader state setup, disposable account/order data, or separate exploratory coverage.

## Shared-Demo and Selector Limitations

The application and its data are controlled externally and may reset or change without notice. Catalog availability, pricing, product-option values, markup, rate limiting, Cloudflare, and other anti-automation controls can affect execution. The suite never attempts to bypass such controls.

An HTTP 403 or challenge response received before the storefront loads is treated as an environment blocker, not as a product failure. Do not suppress that signal with `failOnStatusCode: false` or introduce browser-fingerprint or anti-bot bypass logic.

Because the portfolio does not control nopCommerce source code, no dedicated `data-*` automation hooks are available. Selectors therefore prioritize stable IDs and semantic class names observed in the approved baseline, with visible text used only for meaningful product and notification behavior. Product attribute IDs are catalog-generated and are the primary known selector limitation.

## Public Demo Execution

- Ten Cypress tests are implemented across four TypeScript specs.
- The TypeScript check passes with `npx tsc --noEmit`.
- Script-driven live browser execution with manual evidence review was completed before the Cypress automation phase.
- Cypress execution against the public demo is blocked at the initial page request by HTTP `403 Forbidden`.
- Zero product assertions were reached. The Cypress runner's ten reported failures are environment-blocked tests, not ten failed product tests.
- The public environment is externally controlled, and no Cloudflare or anti-bot bypass was attempted.

## Controlled Local Execution

A controlled local nopCommerce target is the preferred deterministic execution environment for this suite. The verified environment uses nopCommerce `4.90.6`, Microsoft SQL Server 2022 CU20 Express, and the official sample catalog at `http://localhost:8080`.

The local sample data contains the same simple product, configurable product and options, search keyword, Shoes category, and Nike manufacturer used by the public-demo fixture, so no fixture values were changed. The local cart quantity control recalculates after the field loses focus; the test uses Cypress retry-ability and retains the approved mathematical subtotal and total assertions. Product text assertions normalize template whitespace without weakening expected values.

Verified controlled-local result:

- TypeScript: PASS
- Cypress tests: 10 executed
- Passed: 10
- Failed: 0
- Environment errors: 0
- Duration: 21 seconds

## GitHub Actions CI

`.github/workflows/cypress.yml` runs on GitHub-hosted `ubuntu-24.04` for pushes and pull requests to `main`, plus manual dispatch. Each run creates an empty Docker Compose project, performs the first-run nopCommerce installation non-interactively with ephemeral credentials and sample data, waits for the controlled storefront and catalog, validates TypeScript, and runs these same ten Cypress tests with `cypress-io/github-action@v7`.

CI does not use a preinstalled database, committed volume, self-hosted runner, Cypress Cloud, or manual setup step. If Cypress fails, available screenshots are uploaded for diagnosis; provisioning failures print Docker Compose status and logs. The workflow must remain failing when environment setup, TypeScript, or a product assertion fails.

Execution distinctions:

- Local controlled environment: Docker Compose → nopCommerce 4.90.6 sample store → 10/10 Cypress passes.
- Public demo: live execution review completed successfully, while Cypress receives HTTP 403; no anti-bot bypass is attempted.
- CI: fresh GitHub-hosted runner → Docker Compose → automated sample-data bootstrap → the same Cypress regression suite. Refer to the actual GitHub Actions run for status.

## Install

From `01-ecommerce-qa-case-study/automation/`:

```bash
npm install
```

## Run

Run all specs headlessly:

```bash
npx cypress run
```

The configured default target is the controlled local store at `http://localhost:8080`. To invoke the optional public smoke target explicitly:

```powershell
$env:CYPRESS_BASE_URL = "https://demo.nopcommerce.com"
npx cypress run
```

Open the Cypress runner for local investigation:

```bash
npm run cy:open
```

Failure screenshots are written under `cypress/screenshots/`. Video recording is disabled. Headless runs retry a failed test once; interactive runs do not retry.
