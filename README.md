# Fernando Michael Panjaitan — Software QA Portfolio

[![Cypress CI](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/cypress.yml/badge.svg?branch=main)](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/cypress.yml)
[![Cypress](https://img.shields.io/badge/Cypress-regression-17202C?logo=cypress&logoColor=white)](01-ecommerce-qa-case-study/automation/)
[![TypeScript](https://img.shields.io/badge/TypeScript-automation-3178C6?logo=typescript&logoColor=white)](01-ecommerce-qa-case-study/automation/)

Quality Assurance / Software Tester portfolio demonstrating manual QA, requirement and test-case design, regression testing, TypeScript automation, QA documentation, controlled test environments, and continuous integration.

## Portfolio Snapshot

| Area | Result |
|---|---|
| Structured discovery | 44 actions |
| Approved requirements | 27 |
| Test scenarios | 39 |
| Selected test cases | 24 |
| Manual execution | 24/24 PASS |
| Cypress regression | 10/10 PASS |
| CI | GitHub Actions — verified PASS |
| Controlled environment | Dockerized nopCommerce + SQL Server |

## Featured Project — E-Commerce QA Case Study

**System:** nopCommerce

**Status:** COMPLETE

**Purpose:** A clean-room, end-to-end QA case study that moves from uncertain product behavior to an approved test baseline, live manual validation, focused regression automation, and repeatable CI execution.

### QA Workflow

`Product discovery` → `Requirement analysis` → `Approved requirements` → `Risk-based scenarios` → `Selected detailed test cases` → `Manual execution` → `Automation candidate selection` → `Cypress regression` → `Controlled Docker environment` → `GitHub Actions CI`

### What This Project Demonstrates

- Deriving testable requirements from incomplete product information.
- Separating observation, assumption, requirement, open-question, and defect reasoning.
- Exploratory, risk-based, state-transition, and business-rule test design.
- Frontend manual regression with traceable execution evidence.
- Cypress regression automation in TypeScript with isolated test setup.
- Mathematical assertions for cart quantity, subtotal, and total behavior.
- A Docker-based controlled test environment with sample catalog data.
- CI provisioning from a fresh environment instead of relying on persistent state.
- Traceability from approved requirements through scenarios, manual cases, and automation.

## Environment Strategy

| Stage | Environment | Decision and Result |
|---|---|---|
| Manual validation | Official public nopCommerce Demo | 24 selected test cases executed; 24 PASS. |
| Initial automation target | Official public nopCommerce Demo | Cypress requests received HTTP 403 before product assertions could execute. This was treated as an externally controlled environment constraint. |
| Engineering decision | Public Demo | No anti-bot bypass or assertion weakening was attempted. |
| Controlled automation | nopCommerce 4.90.6 + SQL Server 2022 CU20 Express | Docker Compose provided a repeatable local application and sample catalog; 10/10 Cypress tests passed. |
| Continuous integration | GitHub-hosted Ubuntu 24.04 runner | A fresh application and database are provisioned, installed, validated, and tested for each workflow execution. |

This separation preserves the validity of the successful public manual execution while giving automation a controlled, reproducible target.

## Key Artifacts

| Artifact | Purpose |
|---|---|
| [Approved requirement baseline](01-ecommerce-qa-case-study/docs/01-product-requirements.md) | 27 approved, testable requirements derived from structured discovery. |
| [Risk-based test scenarios](01-ecommerce-qa-case-study/docs/02-test-scenarios.md) | 39 concise scenarios with requirement coverage and priority. |
| [Selected detailed test cases](01-ecommerce-qa-case-study/test-cases/03-selected-test-cases.xlsx) | 24 execution-ready cases selected by risk and regression value. |
| [Live test execution workbook](01-ecommerce-qa-case-study/test-cases/04-live-test-execution.xlsx) | Final manual results, actual outcomes, and evidence references. |
| [Live execution summary](01-ecommerce-qa-case-study/docs/04-live-execution-summary.md) | Concise report of the 24/24 PASS manual execution. |
| [Cypress automation](01-ecommerce-qa-case-study/automation/) | TypeScript suite, traceability, test data, and execution guidance. |
| [Controlled test environment](01-ecommerce-qa-case-study/test-environment/) | Reproducible nopCommerce and SQL Server deployment using Docker Compose. |
| [GitHub Actions workflow](.github/workflows/cypress.yml) | Fresh-environment provisioning, validation, and regression execution. |

## Automation Summary

The suite contains 10 selected regression checks across:

- Authentication
- Product Discovery
- Product Detail
- Cart

Each test establishes its own preconditions and maps to a manual test case, scenario, and approved requirement. The suite avoids credentials, persistent accounts, execution-order dependencies, fixed waits, and checkout side effects.

Manual coverage is intentionally retained for account creation and authenticated flows, broader product discovery, cart synchronization and removal, checkout, and order completion. See the [automation README](01-ecommerce-qa-case-study/automation/README.md) for full traceability and execution details.

## GitHub Actions CI

`Push / pull request` → `GitHub-hosted Ubuntu runner` → `Docker Compose` → `SQL Server + nopCommerce` → `Automated first-run installation` → `Sample catalog validation` → `TypeScript check` → `Cypress regression` → `Failure screenshots when necessary`

Verified CI run: [10/10 Cypress tests passed on GitHub Actions](https://github.com/ndo-fer/software-qa-portfolio/actions/runs/31572314690).

## Project Structure

```text
software-qa-portfolio/
├── .github/workflows/
├── 01-ecommerce-qa-case-study/
│   ├── docs/
│   ├── test-cases/
│   ├── evidence/
│   ├── automation/
│   └── test-environment/
├── 02-legacy-erp-analysis-case-study/
├── 03-api-testing-case-study/
└── 04-selenium-case-study/
```

## Other Portfolio Projects

| Project | Status |
|---|---|
| 2. Legacy ERP Migration Analysis | **Planned / Next** |
| 3. REST API Testing | **Planned** |
| 4. Selenium Case Study | **Optional / Future** |

## About Me

I am **Fernando Michael Panjaitan**, a Quality Assurance / Software Tester focused on reliable software delivery through clear requirements, thoughtful test design, evidence-based execution, and maintainable regression coverage.

My experience themes include manual and automation testing, test-case design, QA documentation, requirement clarification, Cypress and Selenium exposure, Git/GitHub workflows, SQL and database familiarity, and cross-functional collaboration.

[Connect with me on LinkedIn](https://linkedin.com/in/fernando-m-p)

## Confidentiality

This is a clean-room portfolio built with public/demo systems and synthetic test data. It contains no employer source code, private internal company artifacts, proprietary documentation, real customer data, passwords, or credentials.
