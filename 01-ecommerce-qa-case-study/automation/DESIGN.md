# Cypress Regression Suite Design

## Purpose

Build a small TypeScript Cypress regression suite for the approved nopCommerce case-study baseline. The suite covers ten isolated checks and intentionally excludes registration, persistent authentication, checkout, and behavior outside approved requirements.

## Architecture

- Four module-focused specs: authentication, discovery, product detail, and cart.
- One fixture for public, non-sensitive catalog paths, keywords, and product configurations.
- Lightweight custom commands for establishing the state required by the current test only.
- No Page Object Model and no journey-dependent execution.
- Cypress configuration uses the shared public demo as `baseUrl`, enables failure screenshots, disables video, and applies one run-mode retry.

## Isolation Model

Every test starts an anonymous browser session and establishes its own cart or page precondition. Helpers may create state within the active test, but no test consumes state produced by another test. Cypress test isolation remains enabled, and the suite does not depend on execution order or persistent demo accounts.

## Assertion Model

Each test asserts approved observable behavior. Cart quantity tests parse currency values and verify mathematical recalculation rather than checking only navigation or button clicks. The suite uses Cypress retry-ability and visible state assertions instead of fixed waits.

## Traceability Scope

The ten tests map to ten selected detailed test cases and cover approved authentication, product-discovery, product-detail, and cart requirements. Full traceability is maintained in `README.md`.

## Shared-Demo Constraints

The target is an externally controlled, shared public demo with periodic resets and potentially changing catalog or anti-automation controls. The suite uses no credentials, destructive actions, account creation, checkout, load testing, or anti-bot bypasses. If the environment blocks Cypress, execution stops and the condition is reported as an environment blocker.
