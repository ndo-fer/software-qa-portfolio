# Legacy ERP Migration Analysis

**Status:** COMPLETE — Legacy ERP Analysis and QA Design

This clean-room case study examines how a long-running desktop ERP could be understood before migration to a browser-based system. It uses the fictional **Northstar Components Manufacturing**, a mid-sized industrial-component manufacturer, and synthetic descriptions throughout.

The selected scope covers Purchasing, Sales, Inventory, Manufacturing, and supporting Master Data and Role Permission capabilities. Finance appears only as a possible downstream impact; detailed accounting is not modeled.

## Project Artifacts

- [Case Context](docs/01-case-context.md) — case facts, scope, migration problem, and analysis objective.
- [Legacy Feature Inventory](docs/02-legacy-feature-inventory.md) — 30 representative clean-room capabilities and their initial migration questions.
- [As-Is Process Flows](docs/03-as-is-process-flows.md) — four high-level working models with assumptions and unresolved questions.
- [Legacy-to-Web Mapping](docs/04-legacy-to-web-mapping.md) — preliminary analyst proposals for translating each capability.
- [Open Question Register](docs/05-open-question-register.md) — 20 questions requiring stakeholder or governance decisions.
- [Stakeholder Decision Baseline](docs/06-stakeholder-decision-baseline.md) — 15 selected high-impact questions translated into fictional V1 decisions or an explicit deferral.
- [Mini System Requirements Document](docs/07-mini-srd.md) — the compact target-system baseline with 13 business rules and 19 functional requirements.
- [Requirement Traceability](docs/08-requirement-traceability.md) — end-to-end mappings and a coverage classification for all 30 Sprint 1 capabilities.
- [QA Test Scenarios](docs/09-qa-test-scenarios.md) — 30 risk-based scenarios covering all 19 approved requirements.
- [Selected ERP Test Cases](test-cases/10-selected-erp-test-cases.xlsx) — 16 detailed design-only cases with scenario and requirement coverage.

## Project Progression

- **Sprint 1 — Legacy reconstruction:** 30 representative capabilities, four As-Is working models, 20 open questions, and preliminary migration proposals.
- **Sprint 2 — Requirement baseline:** 15 selected decision points, 13 business rules, 19 functional requirements, and end-to-end requirement traceability.
- **Sprint 3 — QA design:** 30 risk-based scenarios and 16 selected detailed test cases covering quantity, state, authorization, cross-module, and data-integrity risks.

## Final Metrics

| Analysis Layer | Result |
|---|---:|
| Legacy capabilities | 30 |
| Original open questions | 20 |
| Selected decision points | 15 |
| Business rules | 13 |
| Functional requirements | 19 |
| QA scenarios | 30 |
| Selected detailed test cases | 16 |

The test cases are **DESIGN ONLY** and were not executed against a real or fictional deployed application. No execution outcome, screenshot, or evidence is claimed.

## Confidentiality Approach

All company details, capability descriptions, flows, and questions were independently created for this fictional scenario. Uncertain behavior is recorded as an assumption or open question rather than presented as fact.

> This project reconstructs a generic migration case from independently created artifacts. It does not reproduce employer/client source code, screenshots, internal documentation, or proprietary business data.
