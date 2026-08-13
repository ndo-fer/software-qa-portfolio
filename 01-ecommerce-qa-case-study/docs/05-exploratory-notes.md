# Exploratory Discovery Notes

## Session Metadata

- **Discovery Date:** 2026-08-11 to 2026-08-12
- **Target:** nopCommerce public demo
- **Execution Mode:** Script-driven browser interaction with manual evidence review
- **Browser:** Chrome via undetected-chromedriver

---

## 1. Key Findings

These notes record observations from a 44-step discovery pass against the public nopCommerce demo. The observations were used to clarify expected behavior before detailed test design. They are observation records, not PASS/FAIL test results, and unexpected behavior is not treated as a defect without an established expectation.

**Follow-up Checks:**
- **AUTH Invalid-Login (`AUTH-OQ-004`):** Live DOM inspection and `AUTH-EV-004.png` confirmed that upon invalid login failure, both Email input (`value=""`) and Password input (`value=""`) are **CLEARED** (Email is NOT PRESERVED), a red error banner `"Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect"` is displayed, and the user remains anonymous.
- **Nike Manufacturer Filter:** On `/shoes`, Filter Label: `Manufacturer = Nike`, Products Before (3): `['adidas Consortium Campus 80s Running Shoes', 'Nike Floral Roshe Customized Running Shoes', 'Nike SB Zoom Stefan Janoski "Medium Mint"']`, Products After (2): `['Nike Floral Roshe Customized Running Shoes', 'Nike SB Zoom Stefan Janoski "Medium Mint"']`, Selected Indicator: `Checkbox #attribute-manufacturer-3 checked (:checked), URL parameter ms=3 appended`. Evidence: `evidence/discovery/discovery/DISC-EV-NIKE.png`.
- **Isolated Cart Check (`CART-OQ-001`):**
  - **STATE C0 (Empty Cart):** Line Count: `0`, Header: `(0)`, Mini-Cart: `You have no items in your shopping cart.`.
  - **STATE C1 (Config A Added, Qty 1):** Line Count: `1`, Qty: `1`, Header: `(1)`, Subtotal: `$1,315.00`, Mini-Cart: `There are 1 item(s) in your cart. | Build your own computer | Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00] | RAM: 2 GB | HDD: 320 GB | OS: Vista Home [+$50.00] | Software: Microsoft Office [+$50.00] | Unit price: $1,315.00 | Quantity: 1 | Sub-Total: $1,315.00 | GO TO CART`.
  - **STATE C2 (Qty Updated 1 -> 2):** Line Count: `1`, Qty: `2`, Header: `(2)`, Subtotal: `$2,630.00`, Mini-Cart: `There are 2 item(s) in your cart. | Build your own computer | Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00] | RAM: 2 GB | HDD: 320 GB | OS: Vista Home [+$50.00] | Software: Microsoft Office [+$50.00] | Unit price: $1,315.00 | Quantity: 2 | Sub-Total: $2,630.00 | GO TO CART`.
  - **STATE C3 (Exact Same Config A Added Again):** Line Count: `1`, Qty: `3`, Attribute Text: `Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00] RAM: 2 GB HDD: 320 GB OS: Vista Home [+$50.00] Software: Microsoft Office [+$50.00]`, Header: `(3)`, Subtotal: `$3,945.00`, Order Total: `Total: $3,945.00`, Mini-Cart: `There are 3 item(s) in your cart. | Build your own computer | Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00] | RAM: 2 GB | HDD: 320 GB | OS: Vista Home [+$50.00] | Software: Microsoft Office [+$50.00] | Unit price: $1,315.00 | Quantity: 3 | Sub-Total: $3,945.00 | GO TO CART`.
  - **`CART-OQ-001` Classification:** `OBSERVED` (`RESOLVED — Identical product addition merged quantity from 2 to 3 on single line item`).
- **Mini-Cart Surface Synchronization (`CART-OQ-005`):** `OBSERVED` (`RESOLVED — Mini-cart flyout rendered visible items consistent with Full Cart and Header Count across all states`).

Discovery boundaries:
- **No requirements were approved.**
- **No PASS/FAIL statuses were assigned.**
- **No defect severities were assigned.**
- **No expected behaviors were invented.**
- **No automation code (Cypress) was initialized or executed.**

---

## 2. Preserved vs Reset State Matrix

| State Dimension | Before | After Filter (Nike) | After Sort | After View Change | After Page Size |
|---|---|---|---|---|---|
| Category | /shoes | Preserved | Preserved | Preserved | Preserved |
| Search Keyword | N/A | N/A | N/A | N/A | N/A |
| Active Filter | None | Manufacturer = Nike (ms=3) | Preserved | Preserved | Preserved |
| Sort | Position / Default | Default | Price: Low to High | Preserved | Preserved |
| View | Grid | Grid | Grid | List | List |
| Page Size | Initial | Preserved | Preserved | Preserved | Updated |

---

## 3. Cart State Follow-up Matrix

| State | Action | Full Cart Lines | Quantity | Header Cart Count | Visible Mini-Cart Flyout | Subtotal / Total | Status / Classification |
|---|---|---|---|---|---|---|---|
| **C0** | Fresh empty cart | 0 | 0 | (0) | You have no items in your shopping cart. | $0.00 | OBSERVED |
| **C1** | Add Config A (Qty 1) | 1 | 1 | (1) | There are 1 item(s) in your cart. | Build your own computer | Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00] | RAM: 2 GB | HDD: 320 GB | OS: Vista Home [+$50.00] | Software: Microsoft Office [+$50.00] | Unit price: $1,315.00 | Quantity: 1 | Sub-Total: $1,315.00 | GO TO CART | $1,315.00 | OBSERVED |
| **C2** | Update Qty 1 -> 2 | 1 | 2 | (2) | There are 2 item(s) in your cart. | Build your own computer | Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00] | RAM: 2 GB | HDD: 320 GB | OS: Vista Home [+$50.00] | Software: Microsoft Office [+$50.00] | Unit price: $1,315.00 | Quantity: 2 | Sub-Total: $2,630.00 | GO TO CART | $2,630.00 | OBSERVED |
| **C3** | Add Exact Same Config A (Qty 1) | 1 | 3 | (3) | There are 3 item(s) in your cart. | Build your own computer | Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00] | RAM: 2 GB | HDD: 320 GB | OS: Vista Home [+$50.00] | Software: Microsoft Office [+$50.00] | Unit price: $1,315.00 | Quantity: 3 | Sub-Total: $3,945.00 | GO TO CART | Subtotal: $3,945.00 / Total: Total: $3,945.00 | OBSERVED |

---

## 4. Follow-up Observation Details

### OBS-AUTH-006 (AUTH-OQ-004)
- **Status:** OBSERVED WITH VALID EVIDENCE
- **Observed Result:** Invalid login clears both Email and Password input fields in the DOM (`value=""`). The user remains anonymous. Red error banner is rendered: `"Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect"`. Email is **NOT PRESERVED** (CLEARED).
- **Evidence Screenshot:** `evidence/discovery/auth/AUTH-EV-004.png`

### OBS-DISC-004-FILT (DISCRIMINATING NIKE FILTER)
- **Status:** OBSERVED WITH VALID EVIDENCE
- **Selected Filter Label:** `Manufacturer = Nike`
- **Filter Value:** `Nike (ms=3)`
- **Products Before (3):** `['adidas Consortium Campus 80s Running Shoes', 'Nike Floral Roshe Customized Running Shoes', 'Nike SB Zoom Stefan Janoski "Medium Mint"']`
- **Products After (2):** `['Nike Floral Roshe Customized Running Shoes', 'Nike SB Zoom Stefan Janoski "Medium Mint"']`
- **URL After Filter:** `https://demo.nopcommerce.com/shoes?viewmode=grid&orderby=0&pagesize=6&ms=3`
- **Selected State Indicator:** `Checkbox #attribute-manufacturer-3 checked (:checked), URL parameter ms=3 appended`
- **Evidence Screenshot:** `evidence/discovery/discovery/DISC-EV-NIKE.png`

### OBS-CART-003 (CART-OQ-001)
- **Status:** OBSERVED
- **Precondition:** C2 verified with 1 line, Qty = 2.
- **Action (C3):** Return to PDP, select exact same Config A, add Qty 1.
- **Observed Result:** Cart displays line count = 1, Qty = 3.
- **Classification / Note:** RESOLVED — Identical product addition merged quantity from 2 to 3 on single line item
- **Evidence Screenshot:** `evidence/discovery/cart/CART-EV-C3-MICRO.png`

### OBS-CART-005 (CART-OQ-005)
- **Status:** OBSERVED
- **Observed Result:** RESOLVED — Mini-cart flyout rendered visible items consistent with Full Cart and Header Count across all states

---

# Discovery Summary

## Checklist Execution Metrics
- **Attempted:** 44/44
- **Completed with recorded observation:** 44/44
- **Traceability gaps:** 0/44

## Open Question Status

The targeted follow-up questions were resolved.

- **Total Original Open Questions:** 39
- **Resolved:** 19
- **Partially Resolved:** 4
- **Needs Clarification:** 16

### Resolved and Partially Resolved Questions
- `AUTH-OQ-004`: **RESOLVED** — Invalid login clears both Email and Password input fields (`value=""`), displays red error summary banner, user remains anonymous. Email is NOT PRESERVED (CLEARED). (Supporting Obs: `OBS-AUTH-006` / `AUTH-EV-004.png`)
- `AUTH-OQ-006`: **RESOLVED** — Protected account pages redirect anonymous users to login page upon navigation after logout. (Supporting Obs: `OBS-AUTH-007`)
- `DISC-OQ-003`: **RESOLVED** — Sort changes update item order while preserving active category context. (Supporting Obs: `OBS-DISC-005-SORT`)
- `DISC-OQ-004`: **RESOLVED** — Zero-result search query renders `"No products were found that matched your criteria."` empty state message. (Supporting Obs: `OBS-DISC-002`)
- `DISC-OQ-007`: **PARTIALLY RESOLVED** — Observed: category, active filter (Nike), and sort state preserved while switching Grid/List view. (Supporting Obs: `OBS-DISC-006-VIEW`). Remaining Gap: Search-query preservation during Grid/List switching was not tested in this flow.
- `DISC-OQ-008`: **PARTIALLY RESOLVED** — Observed: page size updated (`pagesize` parameter), category/filter/sort state preserved. (Supporting Observation: `OBS-DISC-007-PAGESIZE`). Remaining Gap: Search-query preservation during page-size change was not tested in this flow.
- `PDP-OQ-001`: **RESOLVED** — Attempting Add to cart without required configuration displays top notification warning and blocks addition. (Supporting Obs: `OBS-PDP-004`)
- `PDP-OQ-003`: **PARTIALLY RESOLVED** — Displayed price dynamically updates between Config A ($1,315.00), Config B ($1,445.00), and default ($1,200.00). Remaining Gap: SKU updates and product main image swaps upon attribute selection not fully evaluated.
- `PDP-OQ-004`: **PARTIALLY RESOLVED** — Apple MacBook Pro PDP exposes a minimum quantity restriction of 2. Remaining Gap: Full accepted quantity range, maximum limits, decimal handling, and product-to-product variation not established.
- `PDP-OQ-007`: **RESOLVED** — Configured products enter cart with distinct attribute summaries appended to product line items. (Supporting Obs: `OBS-PDP-005` / `OBS-CART-002`)
- `CART-OQ-001`: **RESOLVED** — Identical product configuration addition merges quantity (Qty 2 -> 3) on single line item. (Supporting Obs: `OBS-CART-003` / `CART-EV-C3-MICRO.png`)
- `CART-OQ-002`: **RESOLVED** — Different product configurations create distinct cart line rows with separate DOM attribute text summaries. (Supporting Obs: `OBS-CART-004`)
- `CART-OQ-003`: **RESOLVED** — Final cart line item removal renders empty cart screen, updates header count to `(0)`, and removes checkout/totals DOM nodes. (Supporting Obs: `OBS-CART-007`)
- `CART-OQ-005`: **RESOLVED** — Full Cart, Header Count, and visible Mini-Cart flyout rendered visible items consistently across all cart states (C0-C3). (Supporting Observation: `OBS-CART-005`)
- `CART-OQ-008`: **RESOLVED** — Selected product attributes update unit price and propagate accurately to subtotal and order totals. (Supporting Obs: `OBS-CART-001` / `OBS-CART-002`)
- `CHK-OQ-001`: **RESOLVED** — Checkout sequence progresses through Billing Address -> Shipping Address -> Shipping Method -> Payment Method -> Payment Information -> Confirm Order. (Supporting Obs: `OBS-CHK-004`)
- `CHK-OQ-002`: **RESOLVED** — Observed: live guest-checkout billing form marked First Name, Last Name, Email, Country, City, Address 1, Zip / Postal Code, Phone as required fields. (Supporting Obs: `OBS-CHK-004`)
- `CHK-OQ-003`: **RESOLVED** — In the tested anonymous checkout flow containing a physical product, Shipping Address and Shipping Method appeared after Billing Address and before Payment Method. (Supporting Obs: `OBS-CHK-004`)
- `CHK-OQ-004`: **RESOLVED** — Guest checkout exposes specific shipping options (Ground, Next Day Air, 2nd Day Air). (Supporting Obs: `OBS-CHK-004`)
- `CHK-OQ-005`: **RESOLVED** — Available payment methods (Check/Money Order, Credit Card) are exposed in checkout flow. (Supporting Obs: `OBS-CHK-004`)
- `CHK-OQ-006`: **RESOLVED** — Demo allows order completion via Check/Money Order without real monetary transactions. (Supporting Obs: `OBS-CHK-005`)
- `CHK-OQ-007`: **RESOLVED** — Order confirmation page displays `"Your order has been successfully processed!"` and assigned order number. (Supporting Obs: `OBS-CHK-005`)
- `CHK-OQ-008`: **RESOLVED** — Post-order cart state returns to empty cart (`line_count=0`, `header=(0)`). (Supporting Obs: `OBS-CHK-006`)

## Evidence Coverage Index

| Step | Module | Observation ID / Record | Execution Summary | Evidence Reference | Status |
|---|---|---|---|---|---|
| 1 | Authentication | OBS-AUTH-001 | Inspect registration form fields and required indicators | Form labels & required `*` indicators observed | OBSERVED — DOM RECORD |
| 2 | Authentication | OBS-AUTH-002 | Register disposable synthetic test account | Submitted registration form with synthetic user data | OBSERVED — DOM RECORD |
| 3 | Authentication | OBS-AUTH-003 | Record registration success behavior | Success message `"Your registration completed"` rendered | OBSERVED — DOM RECORD |
| 4 | Authentication | OBS-AUTH-004 | Log out from authenticated session | Clicked logout link, anonymous header restored | OBSERVED — DOM RECORD |
| 5 | Authentication | OBS-AUTH-005 | Log in using newly created synthetic account | Submitted valid credentials, header updated to account link | OBSERVED — DOM RECORD |
| 6 | Authentication | OBS-AUTH-006 | Submit invalid login credentials | Used the valid synthetic test-account email with one intentionally incorrect password; login failed and both credential fields were cleared | OBSERVED — SCREENSHOT (`evidence/discovery/auth/AUTH-EV-004.png`) |
| 7 | Authentication | OBS-AUTH-006 | Record invalid login error behavior | Error summary rendered, Email and Password cleared (`value=""`) | OBSERVED — FOLLOW-UP CHECK |
| 8 | Authentication | OBS-AUTH-007 | Access protected page after logout | Direct navigation to `/customer/info` redirects to `/login` | OBSERVED — DOM RECORD |
| 9 | Product Discovery | OBS-DISC-001 | Simple search with known product keyword | Submitted query `"computer"`, matching product set displayed (`Build your own computer` returned) | OBSERVED — DOM RECORD |
| 10 | Product Discovery | OBS-DISC-002 | Simple search returning no products | Submitted query `"zzqaportfolio20260811231914"`, empty state rendered | OBSERVED — DOM RECORD |
| 11 | Product Discovery | OBS-DISC-003 | Inspect Advanced Search form controls | Category, subcategory, manufacturer filters exposed | OBSERVED — DOM RECORD |
| 12 | Product Discovery | OBS-DISC-004 | Advanced Search category constraint | Keyword: `computer` \| Category: `Computers` \| Automatically search sub categories: `enabled` | OBSERVED — DOM RECORD |
| 13 | Product Discovery | OBS-DISC-005 | Open category page exposing filters | Navigated to `/shoes` category page | OBSERVED — SCREENSHOT (`evidence/discovery/discovery/DISC-EV-NIKE.png`) |
| 14 | Product Discovery | OBS-DISC-004-FILT | Apply manufacturer filter | Selected `Nike` (`ms=3`), reduced product count 3 -> 2 | OBSERVED — SCREENSHOT (`evidence/discovery/discovery/DISC-EV-NIKE.png`) |
| 15 | Product Discovery | OBS-DISC-005-SORT | Change sort order | Applied `Price: Low to High` sorting | OBSERVED — DOM RECORD |
| 16 | Product Discovery | OBS-DISC-006-VIEW | Switch Grid/List view mode | Toggled Grid view to List view mode | OBSERVED — DOM RECORD |
| 17 | Product Discovery | OBS-DISC-007-PAGESIZE | Change page size dropdown | Selected page size `3` (previous: `6`), URL updated (`pagesize=3`), display count adjusted to 3, category/filter/sort state preserved | OBSERVED — FOLLOW-UP CHECK |
| 18 | Product Discovery | OBS-DISC-007-PAGESIZE | Record state preservation across layout changes | Category, filter, and sort preserved across view/page-size changes | OBSERVED — FOLLOW-UP CHECK |
| 19 | Product Detail | OBS-PDP-001 | Open simple non-configurable product | Opened product page for `Digital Storm VANQUISH Custom Performance PC` (SKU: `DS_VA3_PC`, Price: `$1,259.00`, simple product, no required attribute choices) | OBSERVED — DOM RECORD |
| 20 | Product Detail | OBS-PDP-002 | Open configurable product page | Opened PDP for `Build your own computer` | OBSERVED — DOM RECORD |
| 21 | Product Detail | OBS-PDP-003 | Record required configuration attributes | Identified required Processor, RAM, HDD, OS attributes (Software optional) | OBSERVED — DOM RECORD |
| 22 | Product Detail | OBS-PDP-004 | Add to cart with incomplete configuration | Clicked Add to Cart without choices, warning notification rendered | OBSERVED — DOM RECORD |
| 23 | Product Detail | OBS-PDP-005 | Select valid product configuration | Configured Config A: Processor 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00], RAM 2 GB, HDD 320 GB, OS Vista Home [+$50.00], Software Microsoft Office [+$50.00] ($1,315.00) | OBSERVED — DOM RECORD |
| 24 | Product Detail | OBS-PDP-006 | Add Config A product to cart | Clicked Add to Cart with Config A | OBSERVED — DOM RECORD |
| 25 | Product Detail | OBS-PDP-006 | Record cart notification and header count | Top green notification bar rendered, header count updated to `(1)` | OBSERVED — DOM RECORD |
| 26 | Cart | OBS-CART-001 | Inspect cart line item representation | Line item rendered with complete attribute summary text | OBSERVED — DOM RECORD |
| 27 | Cart | OBS-CART-002 | Change line item quantity | Updated line item Qty from 1 to 2, subtotal updated | OBSERVED — DOM RECORD |
| 28 | Cart | OBS-CART-003 | Add same exact configuration again | Re-added identical Config A from PDP (Qty 1) | OBSERVED — DOM RECORD |
| 29 | Cart | OBS-CART-003 | Record quantity merge/increment behavior | Line items merged into single row, Qty incremented to 3 | OBSERVED — SCREENSHOT (`evidence/discovery/cart/CART-EV-C3-MICRO.png`) |
| 30 | Cart | OBS-CART-004 | Add different configuration of same product | Configured Config B: Processor 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00], RAM 4GB [+$20.00], HDD 400 GB [+$100.00], OS Vista Premium [+$60.00], Software Microsoft Office [+$50.00] ($1,445.00) and added to cart. Evidence: `PDP-EV-001-CONFIGB.png`, `CART-EV-003.png` | OBSERVED — DOM RECORD |
| 31 | Cart | OBS-CART-004 | Record configuration identity representation | Created separate cart line item row for Config B | OBSERVED — DOM RECORD |
| 32 | Cart | OBS-CART-005 | Add another unrelated product | Added `Lenovo IdeaCentre` to cart | OBSERVED — DOM RECORD |
| 33 | Cart | OBS-CART-006 | Remove one item from multi-item cart | Selected Remove on Config B line, updated cart table | OBSERVED — DOM RECORD |
| 34 | Cart | OBS-CART-007 | Remove final remaining item | Removed final line item from shopping cart | OBSERVED — DOM RECORD |
| 35 | Cart | OBS-CART-007 | Record empty cart state | Rendered `"Your Shopping Cart is empty!"` screen, header `(0)` | OBSERVED — SCREENSHOT (`evidence/discovery/cart/CART-EV-004.png`) |
| 36 | Cart | OBS-CART-005 | Observe header, mini-cart, and full-cart sync | Header count, mini-cart flyout, and cart page synchronized (C0-C3) | OBSERVED — DOM RECORD |
| 37 | Checkout | OBS-CHK-001 | Prepare nonempty cart | Added item to cart, accepted terms of service | OBSERVED — DOM RECORD |
| 38 | Checkout | OBS-CHK-002 | Start checkout unauthenticated | Clicked Checkout anonymously from cart page | OBSERVED — DOM RECORD |
| 39 | Checkout | OBS-CHK-002 | Record guest/registration/login choices | Checkout lander rendered Checkout as Guest button | OBSERVED — DOM RECORD |
| 40 | Checkout | OBS-CHK-003 | Guest checkout step sequence | Accordion flow loaded Billing, Shipping, Payment steps | OBSERVED — DOM RECORD |
| 41 | Checkout | OBS-CHK-004 | Record required fields and available steps | Billing required fields recorded, shipping options listed | OBSERVED — DOM RECORD |
| 42 | Checkout | OBS-CHK-005 | Non-real-payment method handling | Selected Check / Money Order payment method | CONDITIONAL SAFE EXECUTION |
| 43 | Checkout | OBS-CHK-005 | Complete demo order safely | Submitted order confirmation | OBSERVED — DOM RECORD |
| 44 | Checkout | OBS-CHK-006 | Record post-order state | Order thank-you page displayed, cart cleared to `(0)` | OBSERVED — DOM RECORD |

## Potential Defects Requiring Clarification
- None
