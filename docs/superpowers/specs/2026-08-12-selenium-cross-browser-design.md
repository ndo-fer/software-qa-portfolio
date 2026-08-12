# Selenium Cross-Browser Automation Design

## Objective

Add a compact fourth portfolio project that demonstrates maintainable Selenium WebDriver automation with Python, pytest, Page Objects, explicit synchronization, isolated browser sessions, and hosted Chrome/Firefox validation against the public SauceDemo site.

The project complements the existing Cypress case study. It does not repeat the broader QA-analysis workflow from Project 1 and does not modify Projects 1-3 test artifacts.

## Scope

The implementation contains exactly nine business-focused UI tests:

1. Valid login.
2. Locked-out user rejection.
3. Logout followed by protected inventory-page access denial.
4. Product sorting by price, low to high.
5. One product added with name and price preserved in the cart.
6. Two products added and one removed with correct remaining state.
7. Required customer-information validation.
8. Successful checkout with confirmation and cleared cart badge.
9. Selected product name and price preserved through cart and checkout overview.

The suite uses only SauceDemo's public demo credentials and does not perform payment, mobile, visual-regression, performance, or browser-cloud testing.

## Architecture

The project lives in `04-selenium-case-study/` and uses four focused Page Objects:

- `LoginPage`: credentials, login submission, visible login errors, and login-page state.
- `InventoryPage`: inventory readiness, product data, sorting, cart mutations, badge state, menu/logout, and cart navigation.
- `CartPage`: cart item data and presence, removal, and checkout navigation.
- `CheckoutPage`: customer-information submission, validation errors, overview item data, completion, and confirmation state.

`BasePage` provides only reusable WebDriver primitives: explicit waits, click, text entry, text reading, element collection, visibility/absence checks, and URL helpers. It contains no business assertions.

Tests call Page Object actions and assert visible business outcomes directly. There is no service layer, god object, ordered-test plugin, retry plugin, or shared authenticated session.

## Locator and Synchronization Policy

Locators prefer stable `data-test` attributes, followed by stable IDs and concise semantic CSS selectors. Product-specific `data-test` selectors are used for deterministic catalog items. Brittle XPath, DOM-position selectors, `nth-child`, and long CSS chains are excluded.

All synchronization uses `WebDriverWait` with Selenium expected conditions such as visibility, clickability, URL state, and collection presence. The suite does not use `time.sleep()` or combine implicit waits with the explicit-wait strategy.

## Browser Lifecycle and CLI

Pytest provides a function-scoped `driver` fixture. Every test creates a new Chrome or Firefox WebDriver and always quits it during teardown, producing a fresh browser profile, cookies, storage, authentication state, and cart state.

The `--browser` option accepts only `chrome` or `firefox`. Local execution is headed by default:

- `pytest --browser chrome`
- `pytest --browser firefox`

Passing `--headless` opts into headless local execution. Chrome uses modern headless mode and both browsers receive a deterministic 1920x1080 desktop viewport. Selenium Manager or system-installed drivers resolve browser drivers; no executable path or `webdriver-manager` dependency is permitted.

## Failure Handling and Reports

A pytest report hook records test outcomes. Fixture teardown captures a PNG only when a test fails, using `screenshots/<browser>-<test-name>.png`. Passing tests produce no screenshots, and generated PNG files remain ignored.

JUnit XML uses pytest's built-in `--junitxml` support and is written as `reports/junit-<browser>.xml`. Generated reports remain ignored while `.gitkeep` files preserve the artifact directories.

## Continuous Integration

`.github/workflows/selenium.yml` runs on Ubuntu 24.04 for relevant pushes, pull requests, and manual dispatches. A non-fail-fast matrix executes Chrome and Firefox independently with Python 3.13 and pinned Selenium 4.46.0 and pytest 9.1.1 dependencies.

Each job prints Python, package, and browser versions, then runs all nine tests with `--headless` and browser-specific JUnit output. JUnit reports upload unconditionally; failure screenshots upload when present. Test failures are not swallowed and no browser-cloud account, Selenium Grid, secret, or anti-bot workaround is used.

## Ownership Boundary

MAIN owns repository architecture, code, Page Objects, pytest fixtures and tests, static validation, local CLI execution, CI, documentation, and Git operations.

WEB owns live SauceDemo behavior verification, DOM and selector verification, browser reproduction, and current-state screenshots. MAIN will not conduct broad live-browser reconnaissance. If the implementation encounters ambiguous live behavior, work stops and a focused WEB handoff identifies only the exact flow, relevant browser, behavior to verify, and observation required.

## Validation and Completion

Before hosted CI, MAIN verifies:

- exactly nine collected tests;
- no `time.sleep`, `webdriver-manager`, hardcoded driver executable, Page Object assertion, private credential, or test-order dependency;
- requirements and workflow syntax;
- available local browser runs and isolated-test samples without claiming unavailable results;
- repository-relative links and ignored generated artifacts.

Completion requires an actual GitHub Actions matrix result with Chrome 9/9 and Firefox 9/9, browser-specific JUnit artifacts, updated Project 4 and root READMEs, a fresh-clone audit, and synchronized local and remote `main`. Any ambiguous live-site behavior is delegated to WEB rather than guessed or broadly investigated by MAIN.
