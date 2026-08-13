# SauceDemo Selenium Cross-Browser Automation

[![Selenium CI](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/selenium.yml/badge.svg?branch=main)](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/selenium.yml)

**BASELINE FINALIZED — Firefox gating, Chrome diagnostic**

## Purpose

This project demonstrates a compact, maintainable Selenium WebDriver suite against the public [SauceDemo](https://www.saucedemo.com/) storefront.

It complements [Project 1](../01-ecommerce-qa-case-study/README.md): Project 1 uses Cypress, TypeScript, Docker, and a controlled application environment; this project emphasizes Python, pytest, Page Objects, isolated browser sessions, and a Chrome/Firefox CI matrix.

## Stack

- Python 3.13
- Selenium 4.46.0
- pytest 9.1.1
- Chrome and Firefox
- GitHub Actions

## Coverage

The suite contains exactly nine tests across authentication, inventory, cart, checkout, session access control, and cross-page product consistency.

| Test | Area | Intent |
|---|---|---|
| Valid login | Authentication | Verify the standard user reaches the inventory page. |
| Locked-out user rejected | Authentication | Verify the public locked identity remains unauthenticated with a visible error. |
| Logout blocks direct inventory access | Session | Verify logout clears access to the protected inventory URL. |
| Sort by price low to high | Inventory | Verify every displayed numeric price is mathematically sorted. |
| Preserve product information in cart | Cart | Verify one selected product keeps its name and price. |
| Add two products and remove one | Cart | Verify badge count and remaining cart contents. |
| Required customer-information validation | Checkout | Verify an empty form produces the first-name requirement. |
| Complete checkout successfully | Checkout | Verify confirmation, completion URL, and cleared cart badge. |
| Preserve item through checkout overview | Cross-page state | Verify the selected name and price across inventory, cart, and overview. |

## Architecture

```text
pytest tests
    -> focused Page Objects
        -> Selenium WebDriver
            -> Chrome / Firefox
```

The four Page Objects own stable locators, user actions, and page-state accessors. Business assertions remain in tests. `BasePage` contains only reusable explicit-wait and interaction primitives.

Every test receives a new function-scoped WebDriver and therefore a fresh browser profile, cookies, local storage, login state, and cart. Synchronization uses `WebDriverWait` and Selenium expected conditions—never fixed sleeps. Selenium Manager or installed system drivers handle driver resolution; no hardcoded path or third-party driver downloader is used.

When a test fails, fixture teardown captures `screenshots/<browser>-<test-name>.png` before closing the browser. Passing tests do not create screenshots.

## Locator Strategy

Selectors prefer stable `data-test` attributes, then stable IDs and concise semantic CSS. Product cards are identified from stable inventory-item containers and product-specific controls use documented `data-test` values. The suite avoids brittle XPath, positional selectors, and long DOM chains.

## Execution

Install the pinned dependencies:

```bash
python -m pip install -r requirements.txt
```

Local runs are visible/headed by default:

```bash
pytest --browser chrome
pytest --browser firefox
```

Headless mode is opt-in locally and mandatory in CI:

```bash
pytest --browser chrome --headless --junitxml reports/junit-chrome.xml
pytest --browser firefox --headless --junitxml reports/junit-firefox.xml
```

## Results

| Environment | Browser | Result | Duration |
|---|---|---:|---:|
| Local, Windows, headless | Chrome 151.0.7922.110 | **9/9 PASS** | 96.93 s |
| Local, Windows, headed targeted | Chrome 151.0.7922.110 | Logout **3/3 PASS**; checkout **3/3 PASS** | — |
| Local, Windows, headed full suite | Chrome 151.0.7922.110 | **8/9 PASS** | 66.17 s |
| Local, Windows, headless | Firefox | **9/9 PASS** | 206.08 s |
| GitHub Actions | Firefox | **9/9 PASS**; required/gating target | — |
| GitHub Actions | Chrome | **4/9 PASS**; experimental/diagnostic target | — |

## Cross-Browser CI Result

Firefox is the required, gating browser and passed **9/9** tests. Chrome remains in the matrix as an experimental diagnostic target. Local final full-suite validation passed **8/9**, while focused Logout and checkout interaction checks each passed **3/3**. The latest hosted Chrome job passed **4/9** and retained its pytest failures and artifacts for diagnosis.

Chrome showed intermittent interaction failures across dynamic menu, cart, and checkout controls. In the accepted local checkout failure, customer-information values were populated but the application did not transition after activation and remained on checkout step one. This is classified as a **HOSTED CHROME AUTOMATION LIMITATION / FLAKY INTERACTION**, not a confirmed SauceDemo defect. No retry, fixed sleep, JavaScript click, browser-specific branch, or pointer-offset workaround was introduced to mask it.

The workflow preserves the Chrome pytest exit and failure artifacts while allowing that experimental matrix job to continue. Firefox remains the required signal. See the [finalized cross-browser run](https://github.com/ndo-fer/software-qa-portfolio/actions/runs/31708257843).

## Artifacts

- [Pinned requirements](requirements.txt)
- [Page Objects](pages/)
- [pytest suite](tests/)
- [Cross-browser workflow](../.github/workflows/selenium.yml)
- Reproducible JUnit XML under `reports/`
- Failure-only screenshots under `screenshots/`

Generated XML and PNG artifacts are ignored locally and uploaded by CI. The empty directories are retained with `.gitkeep` files.

## Limitations

- The target is a public demo application whose source and availability are outside this repository's control.
- Demo credentials are publicly documented SauceDemo test data.
- Coverage targets desktop Chrome and Firefox only.
- Mobile/responsive, visual-regression, accessibility, performance, and browser-cloud testing are outside scope.

## Confidentiality

This project uses only a public demo system and public demo identities. It contains no employer/client artifacts, personal credentials, API keys, or private data.
