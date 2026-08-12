# Live Test Execution Summary

## Environment
- **Target URL:** https://demo.nopcommerce.com/
- **Browser Environment:** Chrome 120 (undetected-chromedriver)
- **Execution Start:** 2026-08-12 05:15:49
- **Execution End:** 2026-08-12 05:21:19
- **Shared-Demo Notes:** Live public demo environment evaluated; state verified before each cart and checkout module flow.

## Result Summary
- **Total Executed:** 24 / 24 selected test cases
- **PASS:** 24
- **FAIL:** 0
- **BLOCKED:** 0
- **INCONCLUSIVE:** 0
- **Defect Candidates:** 0

## Results by Module

### 1. Authentication (4 cases)
- `TC-AUTH-001`: **PASS** — Submitted valid registration form for synthetic test account. Storefront rendered confirmation message 'Your registration completed' on page /registerresult/1 and header navigation updated displaying 'My account' (a.ico-account) and 'Log out' (a.ico-logout) actions.
- `TC-AUTH-002`: **PASS** — Submitted valid login credentials for synthetic test account. Storefront authenticated user and header navigation updated displaying 'My account' (a.ico-account) and 'Log out' (a.ico-logout) links.
- `TC-AUTH-003`: **PASS** — Submitted valid email with invalid password. Login was rejected, displaying error summary banner 'Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect'. Post-failure Email input value was cleared ('') and Password input value was cleared (''). User remained anonymous.
- `TC-AUTH-004`: **PASS** — Direct URL navigation to /customer/info while anonymous was blocked, and browser was redirected to https://demo.nopcommerce.com/login?returnUrl=%2Fcustomer%2Finfo.

### 2. Product Discovery (6 cases)
- `TC-DISC-001`: **PASS** — Navigated to top-level category /computers (Breadcrumbs: 'Home /Computers') and subcategory /notebooks (Breadcrumbs: 'Home / Computers /Notebooks'). Both pages displayed category titles, breadcrumb trails, and assigned product list (6 products).
- `TC-DISC-002`: **PASS** — Submitted simple search query 'computer'. Returned product listing page displaying 4 matching products containing the keyword.
- `TC-DISC-003`: **PASS** — Submitted zero-result query 'zzqaportfolio20260812051600'. The storefront rendered empty state message 'No products were found that matched your criteria.'.
- `TC-DISC-004`: **PASS** — Executed Advanced Search with query 'computer', Category 'Computers', and subcategories enabled. Returned 1 matching products constrained to the category hierarchy.
- `TC-DISC-005`: **PASS** — Selected manufacturer filter 'Nike' on /shoes (URL parameter ms=3 verified). Non-matching product 'adidas Consortium Campus 80s Running Shoes' was removed from display and product listing filtered from 3 items to 2 Nike items ('Nike Floral Roshe Customized Running Shoes', 'Nike SB Zoom Stefan Janoski "Medium Mint"').
- `TC-DISC-006`: **PASS** — Selected sort option 'Price: Low to High' on /shoes page. Products were reordered by ascending price ($27.56, $30.00, $40.00) while maintaining active category breadcrumbs ('Home / Apparel /Shoes').

### 3. Product Detail & Configuration (3 cases)
- `TC-PDP-001`: **PASS** — Opened simple PDP. Displayed product title 'Digital Storm VANQUISH Custom Performance PC', SKU 'DS_VA3_PC', price '$1,259.00', quantity input, and active 'Add to cart' button without requiring option selection.
- `TC-PDP-002`: **PASS** — Clicked Add to cart with incomplete required attributes. Cart addition was blocked and top error notification displayed 'Please select RAM\nPlease select HDD'.
- `TC-PDP-003`: **PASS** — Selected the execution configuration (Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00], RAM: 8GB [+$60.00], HDD: 400 GB [+$100.00], OS: Vista Premium [+$60.00], Software: Microsoft Office [+$50.00]). The displayed product price updated to '$1,485.00'. Added the configured product to cart; the green notification bar 'The product has been added to your shopping cart' appeared and the header cart count incremented from (0) to (1).

### 4. Cart (6 cases)
- `TC-CART-001`: **PASS** — Updated cart line item quantity from 1 to 2 and clicked update cart. Quantity input updated to 2, unit price maintained at $1,259.00, line subtotal recalculated from $1,259.00 to $2,518.00, and total cart order summary updated to Total: $2,518.00.
- `TC-CART-002`: **PASS** — Precondition verified with 2 distinct cart rows ('Digital Storm VANQUISH Custom Performance PC' and 'Build your own computer', Total: $2,744.00, Badge: (2)). Clicked remove on Row 1; target line item was removed, remaining line item retained ('Build your own computer'), header badge updated to (1), and order total recalculated to Total: $1,485.00.
- `TC-CART-003`: **PASS** — Removed final item from cart. Storefront rendered empty cart message 'Your Shopping Cart is empty!', header cart count reset to (0), and order summary/checkout actions were hidden.
- `TC-CART-004`: **PASS** — Verified 3 cart surfaces (full cart table, header badge, mini-cart flyout) across item addition (Header: (1), Flyout: 'There are 1 item(s) in your cart. Digital Storm VA...'), quantity update 1->2 (Header: (2), Flyout: 'There are 2 item(s) in your cart. Digital Storm VA...'), and item removal (Header: (0), Flyout: 'You have no items in your shopping cart.'). All three surfaces synchronized state immediately throughout the session.
- `TC-CART-005`: **PASS** — Added the identical execution configuration to cart a second time. The addition merged into the single existing line-item row by incrementing quantity to 2 rather than creating a duplicate row.
- `TC-CART-006`: **PASS** — Added two distinct execution configurations of the same base product. The first used Processor: 2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00], RAM: 8GB [+$60.00], HDD: 400 GB [+$100.00], OS: Vista Premium [+$60.00], and Microsoft Office [+$50.00]. The second used Processor: 2.2 GHz Intel Pentium Dual-Core E2200, RAM: 4GB [+$20.00], HDD: 320 GB, OS: Vista Home [+$50.00], and Microsoft Office [+$50.00]. The storefront created two separate cart rows with their distinct attribute summaries.

### 5. Checkout (5 cases)
- `TC-CHK-001`: **PASS** — Accepted Terms of Service and clicked Checkout. Lander displayed 'Checkout as Guest', 'Register', and 'Returning Customer' choices. Selecting Checkout as Guest initiated guest checkout at https://demo.nopcommerce.com/onepagecheckout#opc-billing.
- `TC-CHK-002`: **PASS** — The guest checkout accordion presented the step sequence Billing Address -> Shipping Address -> Shipping Method -> Payment Method -> Payment Information -> Confirm Order. First Name, Last Name, Email, Country, City, Address 1, Zip/Postal Code, and Phone were marked as required fields.
- `TC-CHK-003`: **PASS** — Shipping Method step exposed options Ground, Next Day Air, 2nd Day Air (Ground ($0.00), Next Day Air ($0.00), 2nd Day Air ($0.00)). Payment Method step exposed Check / Money Order and Credit Card options (Check / Money Order Pay by cheque or money order, Credit Card Pay by credit / debit card) prior to order review.
- `TC-CHK-004`: **PASS** — Submitted order confirmation using Check / Money Order. The order was processed without external payment gateway interaction. The completion page displayed 'Thank you', 'Your order has been successfully processed!', and ORDER NUMBER: 8.
- `TC-CHK-005`: **PASS** — Inspected shopping cart immediately following guest order completion. The active cart was cleared (line item count = 0, 'Your Shopping Cart is empty!') and header cart count badge restored to (0).

## Defect Candidates
No defect candidates were identified during targeted live execution repair. All 24 selected test cases passed strict evidence validation against the live nopCommerce demo environment.


## Environment Events
- No unexpected shared-demo resets or environment failures interfered with execution.
- All test case preconditions were verified and rebuilt prior to module test execution.

## Evidence Index
- `TC-AUTH-001` → `evidence/execution/auth/EXEC-TC-AUTH-001.png`
- `TC-AUTH-002` → `evidence/execution/auth/EXEC-TC-AUTH-002.png`
- `TC-AUTH-003` → `evidence/execution/auth/EXEC-TC-AUTH-003.png`
- `TC-AUTH-004` → `evidence/execution/auth/EXEC-TC-AUTH-004.png`
- `TC-CART-001` → `evidence/execution/cart/EXEC-TC-CART-001.png`
- `TC-CART-002` → `evidence/execution/cart/EXEC-TC-CART-002.png`
- `TC-CART-003` → `evidence/execution/cart/EXEC-TC-CART-003.png`
- `TC-CART-004` → `evidence/execution/cart/EXEC-TC-CART-004.png`
- `TC-CART-005` → `evidence/execution/cart/EXEC-TC-CART-005.png`
- `TC-CART-006` → `evidence/execution/cart/EXEC-TC-CART-006.png`
- `TC-CHK-001` → `evidence/execution/checkout/EXEC-TC-CHK-001.png`
- `TC-CHK-002` → `evidence/execution/checkout/EXEC-TC-CHK-002.png`
- `TC-CHK-003` → `evidence/execution/checkout/EXEC-TC-CHK-003.png`
- `TC-CHK-004` → `evidence/execution/checkout/EXEC-TC-CHK-004.png`
- `TC-CHK-005` → `evidence/execution/checkout/EXEC-TC-CHK-005.png`
- `TC-DISC-001` → `evidence/execution/discovery/EXEC-TC-DISC-001.png`
- `TC-DISC-002` → `evidence/execution/discovery/EXEC-TC-DISC-002.png`
- `TC-DISC-003` → `evidence/execution/discovery/EXEC-TC-DISC-003.png`
- `TC-DISC-004` → `evidence/execution/discovery/EXEC-TC-DISC-004.png`
- `TC-DISC-005` → `evidence/execution/discovery/EXEC-TC-DISC-005.png`
- `TC-DISC-006` → `evidence/execution/discovery/EXEC-TC-DISC-006.png`
- `TC-PDP-001` → `evidence/execution/product/EXEC-TC-PDP-001.png`
- `TC-PDP-002` → `evidence/execution/product/EXEC-TC-PDP-002.png`
- `TC-PDP-003` → `evidence/execution/product/EXEC-TC-PDP-003.png`
