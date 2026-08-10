# E-Commerce QA Case Study

## 1. Context

This clean-room case study will demonstrate requirement analysis, exploratory testing, formal test design, manual execution, defect reasoning, regression planning, and—only in a later sprint—UI automation.

## 2. Objective

Build an interview-defensible QA case study whose conclusions are traceable to approved requirements, public evidence, explicit human decisions, and genuine test observations.

## 3. System Under Test

- **Application:** nopCommerce Demo storefront
- **Frontend:** <https://demo.nopcommerce.com/>
- **Official demo information:** <https://www.nopcommerce.com/en/demo>
- **Selection status:** Explicitly selected by the portfolio owner for Sprint 1
- **Selection rationale:** The storefront provides broad e-commerce behavior across authentication, search, filtering, product configuration, cart, wishlist, comparison, and checkout.

## 4. Test-Environment Constraints

The nopCommerce demo is a shared public environment. The official demo page states that other users may change its data and that the environment resets to its original state every hour.

Consequences for this case study:

- test data must be public-safe and disposable;
- persistent users, carts, wishlists, orders, or configuration cannot be assumed;
- required preconditions must be checked at the start of each session;
- observations must identify the session context and time;
- unexpected state changes must be distinguished from reproducible product behavior;
- environment instability must not be reported as a product defect without supporting evidence.

## 5. Expected-Behavior Evidence Rule

Expected behavior will not be invented. It may be derived only from:

1. an approved portfolio requirement;
2. clearly supported public product behavior; or
3. an explicit human decision.

If none of these sources establishes the expected behavior, the item will be marked **NEEDS CLARIFICATION** and will not be classified as a confirmed defect.

## 6. Sprint Status

Repository setup and target selection are complete. Product requirements, exploratory observations, and test scenarios have not yet been written and remain subject to the playbook's human checkpoints.

## 7. Confidentiality Notice

This project uses only a public demo application and synthetic, non-confidential data. It contains no employer source code, credentials, internal documents, private screenshots, customer information, or proprietary business rules.
