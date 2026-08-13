# Software QA Portfolio

[![Cypress CI](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/cypress.yml/badge.svg?branch=main)](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/cypress.yml)
[![Postman API CI](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/postman-api.yml/badge.svg?branch=main)](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/postman-api.yml)

QA portfolio covering requirement analysis, test design, execution review, Cypress/Selenium automation, API testing, and CI. Each case study links to the artifacts, code, and run evidence behind its results.

## Start Here

1. [E-Commerce QA Case Study](01-ecommerce-qa-case-study/README.md)
2. [Selenium Cross-Browser Automation](04-selenium-case-study/README.md)
3. [REST API Testing](03-api-testing-case-study/README.md)

## Portfolio Highlights

- Traced 27 approved e-commerce requirements into 39 scenarios, 24 script-driven live executions, and selected screenshot evidence.
- Automated 10 Cypress regression checks against a controlled nopCommerce Docker environment; local and hosted runs passed 10/10.
- Built nine Selenium/pytest tests with Page Objects, explicit waits, isolated sessions, failure screenshots, and JUnit output.
- Established Firefox as the Selenium CI gate at 9/9 while retaining Chrome as a transparent diagnostic target for an intermittent interaction limitation.
- Implemented a Restful Booker Postman suite with 19 requests, 47 passing assertions, authenticated CRUD, schema checks, cleanup, and hosted CI.
- Mapped a fictional legacy ERP migration through requirements, traceability, risk-based scenarios, and 16 design-only test cases.

## Project Index

| Project | Focus | Stack / Techniques | Evidence |
|---|---|---|---|
| [E-Commerce QA Case Study](01-ecommerce-qa-case-study/README.md) | Requirement discovery, test design, live execution review, regression automation | Cypress, TypeScript, Docker Compose, risk-based testing, GitHub Actions | 24/24 reviewed live execution; 10/10 Cypress; [hosted run](https://github.com/ndo-fer/software-qa-portfolio/actions/runs/31572314690) |
| [Selenium Cross-Browser Automation](04-selenium-case-study/README.md) | Isolated UI flows across authentication, inventory, cart, and checkout | Python 3.13, pytest, Selenium, Page Objects, explicit waits, JUnit | Firefox 9/9 gating; local Chrome 8/9 full-suite baseline; [diagnostic matrix](https://github.com/ndo-fer/software-qa-portfolio/actions/runs/31708257843) |
| [REST API Testing](03-api-testing-case-study/README.md) | Authenticated CRUD, negative authorization, contracts, cleanup | Postman CLI, JSON Schema, dynamic test data, GitHub Actions | 19 requests; 47/47 assertions; [hosted run](https://github.com/ndo-fer/software-qa-portfolio/actions/runs/31580305791) |
| [Legacy ERP Analysis](02-legacy-erp-analysis-case-study/README.md) | Clean-room migration analysis and QA design | Process mapping, requirements, traceability, risk-based scenarios | 19 requirements; 30 scenarios; 16 design-only cases |

## Skills Demonstrated

- **QA Analysis:** exploratory analysis, test design, execution review, evidence capture, defect/limitation reporting
- **Automation:** Cypress/TypeScript, Selenium/Python/pytest, Postman CLI, Page Object pattern
- **Test Design:** requirements analysis, traceability, risk-based scenarios, positive/negative testing, API contracts
- **CI / Engineering Workflow:** Git, GitHub Actions, Docker Compose, isolated test data, JUnit artifacts, failure diagnostics

## Confidentiality

This portfolio uses public demo systems, fictional business scenarios, synthetic data, and independently created artifacts. It contains no employer/client source code, private documentation, real customer data, or personal credentials.

[Connect with me on LinkedIn](https://linkedin.com/in/fernando-m-p)
