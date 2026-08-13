# nopCommerce E-Commerce QA Case Study

**Status:** COMPLETE — Test Design, Live Execution Review, Cypress Automation, and CI

## Project Summary

This clean-room case study follows a QA workflow against the public nopCommerce demo: structured product discovery, requirement and risk-based test design, script-driven live browser execution with manual evidence review, regression selection, Cypress automation, a controlled Docker target, and verified GitHub Actions execution.

## Final Metrics

| Evidence | Result |
|---|---:|
| Structured discovery | 44 actions |
| Approved requirements | 27 |
| Test scenarios | 39 |
| Selected detailed test cases | 24 |
| Reviewed live execution | 24/24 PASS |
| Cypress regression | 10/10 PASS |
| GitHub Actions | 10/10 PASS |

## QA Workflow

`Discovery` → `Requirement baseline` → `Risk-based scenarios` → `Detailed test cases` → `Script-driven live execution` → `Evidence review` → `Automation selection` → `Cypress` → `Controlled Docker environment` → `GitHub Actions`

## Environment Strategy

Script-driven browser execution with manual evidence review succeeded against the public nopCommerce demo. Cypress traffic to that externally controlled target received HTTP 403 before product assertions could run; no anti-bot bypass or assertion weakening was attempted.

Automation therefore runs against a deterministic Docker Compose environment using nopCommerce 4.90.6 and Microsoft SQL Server 2022 CU20 Express. The sample catalog matches the suite’s test data and can be provisioned from a fresh environment locally or in CI.

## Key Artifacts

- [Approved product requirements](docs/01-product-requirements.md)
- [Risk-based test scenarios](docs/02-test-scenarios.md)
- [Selected test cases](test-cases/03-selected-test-cases.xlsx)
- [Live test execution workbook](test-cases/04-live-test-execution.xlsx)
- [Live execution summary](docs/04-live-execution-summary.md)
- [Cypress automation](automation/)
- [Automation guide](automation/README.md)
- [Controlled test environment](test-environment/)
- [Environment and reproduction guide](test-environment/README.md)

## Automation and Execution Results

The ten Cypress regression checks cover Authentication, Product Discovery, Product Detail, and Cart behavior.

- Reviewed live execution: **24/24 PASS**
- Controlled local Cypress: **10/10 PASS**
- GitHub Actions: **10/10 PASS** — [canonical hosted run](https://github.com/ndo-fer/software-qa-portfolio/actions/runs/31572314690)

For reproduction, use the [controlled-environment guide](test-environment/README.md) and [automation guide](automation/README.md); they contain the setup, run, configuration, and troubleshooting details.

## Limitations

- The public demo is shared, externally controlled, and periodically reset.
- Public-demo Cypress traffic was blocked with HTTP 403; no anti-bot bypass was used.
- The first Cypress regression suite intentionally excludes state-heavy account-creation and checkout flows; those flows remain covered by the separate live execution set and evidence review.

## Confidentiality

This project uses only public systems, synthetic data, and independently created clean-room artifacts. It contains no private employer/client source code, credentials, screenshots, documentation, or customer data.
