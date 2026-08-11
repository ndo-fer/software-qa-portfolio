# nopCommerce Test Scenarios

This inventory translates only the 27 requirements in `01-product-requirements.md` Section 9, **Approved Requirements**, into concise, risk-based test scenarios. It contains no execution results, detailed test steps, or rules outside the approved baseline.

## Scenario Inventory

| Scenario ID | Requirement ID | Module | Test Scenario | Type | Priority |
|---|---|---|---|---|---|
| SCN-AUTH-001 | REQ-AUTH-001 | Authentication | Verify an anonymous user can open the registration form and see the approved personal-data fields with mandatory fields visually marked. | POSITIVE | P2 |
| SCN-AUTH-002 | REQ-AUTH-002 | Authentication | Verify valid, unique registration data creates an account and displays the approved registration-completion confirmation. | POSITIVE | P1 |
| SCN-AUTH-003 | REQ-AUTH-003 | Authentication | Verify valid registered credentials establish an authenticated session and change the header to show the customer account link and Log out action. | STATE TRANSITION | P1 |
| SCN-AUTH-004 | REQ-AUTH-004 | Authentication | Verify invalid or unrecognized credentials are rejected and the user remains anonymous. | NEGATIVE | P1 |
| SCN-AUTH-005 | REQ-AUTH-004 | Authentication | Verify rejected authentication displays the approved unsuccessful-login error summary. | NEGATIVE | P2 |
| SCN-AUTH-006 | REQ-AUTH-004 | Authentication | Verify rejected authentication clears both Email and Password fields. | NEGATIVE | P2 |
| SCN-AUTH-007 | REQ-AUTH-005 | Authentication | Verify direct anonymous access to the approved protected customer-information URL is blocked and redirected to `/login`. | STATE TRANSITION | P1 |
| SCN-DISC-001 | REQ-DISC-001 | Product Discovery | Verify top-level and subcategory navigation opens the selected category with its title, breadcrumb, and assigned products. | POSITIVE | P2 |
| SCN-DISC-002 | REQ-DISC-002 | Product Discovery | Verify submitting a known product-title keyword returns a listing containing products matching that keyword. | POSITIVE | P2 |
| SCN-DISC-003 | REQ-DISC-003 | Product Discovery | Verify a zero-match simple search displays the approved no-products-found empty state. | NEGATIVE | P2 |
| SCN-DISC-004 | REQ-DISC-004 | Product Discovery | Verify Advanced Search with a keyword, category constraint, and subcategory option returns products matching the keyword and selected category hierarchy. | BUSINESS RULE | P2 |
| SCN-DISC-005 | REQ-DISC-005 | Product Discovery | Verify selecting an available manufacturer filter restricts the category listing to products matching that manufacturer option. | BUSINESS RULE | P2 |
| SCN-DISC-006 | REQ-DISC-006 | Product Discovery | Verify selecting a catalog sort option reorders the displayed product set by the selected criterion without leaving the active category. | INTEGRATION | P2 |
| SCN-DISC-007 | REQ-DISC-007 | Product Discovery | Verify Grid/List switching changes product-item layout while retaining the active category, manufacturer filter, and sort state. | INTEGRATION | P3 |
| SCN-DISC-008 | REQ-DISC-008 | Product Discovery | Verify changing page size adjusts visible products per page, records `pagesize=N` in the URL, and retains active category, filter, and sort state. | INTEGRATION | P3 |
| SCN-PDP-001 | REQ-PDP-001 | Product Detail | Verify an approved simple non-configurable product displays title, SKU, price, and quantity input. | POSITIVE | P2 |
| SCN-PDP-002 | REQ-PDP-001 | Product Detail | Verify a simple non-configurable product exposes an active Add to cart action without requiring option selection. | BUSINESS RULE | P1 |
| SCN-PDP-003 | REQ-PDP-002 | Product Detail | Verify attempting to add a configurable product without all mandatory attributes is blocked and displays a top error notification. | NEGATIVE | P1 |
| SCN-PDP-004 | REQ-PDP-003 | Product Detail | Verify selecting configured-product attributes with approved surcharges dynamically updates the displayed product price. | BUSINESS RULE | P1 |
| SCN-PDP-005 | REQ-PDP-003 | Product Detail | Verify adding a valid configured product updates the cart, displays the approved success notification, and increments the header cart count. | INTEGRATION | P1 |
| SCN-CART-001 | REQ-CART-001 | Cart | Verify updating a cart line quantity recalculates both its line subtotal and the overall cart total. | BUSINESS RULE | P1 |
| SCN-CART-002 | REQ-CART-002 | Cart | Verify removing a selected line from a multi-item cart retains all other cart lines. | STATE TRANSITION | P1 |
| SCN-CART-003 | REQ-CART-002 | Cart | Verify multi-item line removal updates the header count and recalculates cart totals. | INTEGRATION | P1 |
| SCN-CART-004 | REQ-CART-003 | Cart | Verify removing the final cart line transitions the cart to the approved empty state and message. | STATE TRANSITION | P1 |
| SCN-CART-005 | REQ-CART-003 | Cart | Verify final-item removal resets the header count to `(0)` and hides the order summary and checkout actions. | INTEGRATION | P1 |
| SCN-CART-006 | REQ-CART-004 | Cart | Verify product addition synchronizes line-item state across the full cart, mini-cart, and header count. | INTEGRATION | P1 |
| SCN-CART-007 | REQ-CART-004 | Cart | Verify quantity update synchronizes item quantity and count state across the full cart, mini-cart, and header. | INTEGRATION | P1 |
| SCN-CART-008 | REQ-CART-004 | Cart | Verify item removal synchronizes the resulting state across the full cart, mini-cart, and header count. | INTEGRATION | P1 |
| SCN-CART-009 | REQ-CART-005 | Cart | Verify adding an identical product configuration again merges it into the existing cart line and increments quantity without creating a duplicate row. | BUSINESS RULE | P1 |
| SCN-CART-010 | REQ-CART-006 | Cart | Verify adding a different configuration of the same base product creates a separate cart line with its specific attribute summary. | BUSINESS RULE | P1 |
| SCN-CHK-001 | REQ-CHK-001 | Checkout | Verify anonymous checkout from a nonempty cart with accepted Terms of Service displays Guest, Register, and Returning Customer/Login entry options. | POSITIVE | P1 |
| SCN-CHK-002 | REQ-CHK-001 | Checkout | Verify selecting Checkout as Guest transitions the anonymous user into the guest checkout process. | STATE TRANSITION | P1 |
| SCN-CHK-003 | REQ-CHK-002 | Checkout | Verify physical-product guest checkout presents the approved Billing-to-Confirm-Order step sequence in order. | STATE TRANSITION | P1 |
| SCN-CHK-004 | REQ-CHK-002 | Checkout | Verify guest billing marks First Name, Last Name, Email, Country, City, Address 1, Zip/Postal Code, and Phone as required. | BUSINESS RULE | P1 |
| SCN-CHK-005 | REQ-CHK-003 | Checkout | Verify guest checkout exposes Ground, Next Day Air, and 2nd Day Air shipping methods after shipping-address confirmation. | POSITIVE | P2 |
| SCN-CHK-006 | REQ-CHK-003 | Checkout | Verify guest checkout exposes Check / Money Order and Credit Card payment options before order review. | POSITIVE | P1 |
| SCN-CHK-007 | REQ-CHK-004 | Checkout | Verify an order using Check / Money Order can be processed without external payment-gateway processing. | INTEGRATION | P1 |
| SCN-CHK-008 | REQ-CHK-004 | Checkout | Verify successful order submission displays the approved confirmation message and assigns a unique order number. | POSITIVE | P1 |
| SCN-CHK-009 | REQ-CHK-005 | Checkout | Verify successful guest-order completion clears active cart lines and resets the header cart count to `(0)`. | STATE TRANSITION | P1 |

## Requirement Coverage Matrix

| Requirement ID | Scenario IDs | Coverage |
|---|---|---|
| REQ-AUTH-001 | SCN-AUTH-001 | COVERED |
| REQ-AUTH-002 | SCN-AUTH-002 | COVERED |
| REQ-AUTH-003 | SCN-AUTH-003 | COVERED |
| REQ-AUTH-004 | SCN-AUTH-004, SCN-AUTH-005, SCN-AUTH-006 | COVERED |
| REQ-AUTH-005 | SCN-AUTH-007 | COVERED |
| REQ-DISC-001 | SCN-DISC-001 | COVERED |
| REQ-DISC-002 | SCN-DISC-002 | COVERED |
| REQ-DISC-003 | SCN-DISC-003 | COVERED |
| REQ-DISC-004 | SCN-DISC-004 | COVERED |
| REQ-DISC-005 | SCN-DISC-005 | COVERED |
| REQ-DISC-006 | SCN-DISC-006 | COVERED |
| REQ-DISC-007 | SCN-DISC-007 | COVERED |
| REQ-DISC-008 | SCN-DISC-008 | COVERED |
| REQ-PDP-001 | SCN-PDP-001, SCN-PDP-002 | COVERED |
| REQ-PDP-002 | SCN-PDP-003 | COVERED |
| REQ-PDP-003 | SCN-PDP-004, SCN-PDP-005 | COVERED |
| REQ-CART-001 | SCN-CART-001 | COVERED |
| REQ-CART-002 | SCN-CART-002, SCN-CART-003 | COVERED |
| REQ-CART-003 | SCN-CART-004, SCN-CART-005 | COVERED |
| REQ-CART-004 | SCN-CART-006, SCN-CART-007, SCN-CART-008 | COVERED |
| REQ-CART-005 | SCN-CART-009 | COVERED |
| REQ-CART-006 | SCN-CART-010 | COVERED |
| REQ-CHK-001 | SCN-CHK-001, SCN-CHK-002 | COVERED |
| REQ-CHK-002 | SCN-CHK-003, SCN-CHK-004 | COVERED |
| REQ-CHK-003 | SCN-CHK-005, SCN-CHK-006 | COVERED |
| REQ-CHK-004 | SCN-CHK-007, SCN-CHK-008 | COVERED |
| REQ-CHK-005 | SCN-CHK-009 | COVERED |
