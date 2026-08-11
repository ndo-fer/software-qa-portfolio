# Product Requirement Discovery

## 1. Scope

This document prepares a focused, interview-defensible requirement baseline for the nopCommerce Demo storefront. It does not attempt to document every nopCommerce capability.

The primary Sprint 1 product story is:

```text
Authentication
→ Product Discovery / Search
→ Product Detail & Configuration
→ Cart
→ Checkout
```

The intended traceability chain is product evidence → human analysis → approved portfolio requirement → exploration → scenario and case design → execution → defect and regression reasoning → later automation selection.

The following are future or secondary coverage and are outside the current baseline unless explicitly approved later: custom wishlists, product comparison, product reviews, gift cards, rental products, digital downloads, vendor registration, blog/newsletter, currency switching, email-a-friend, and advanced account management.

## 2. Evidence Policy

| Classification | Meaning |
|---|---|
| PUBLIC PRODUCT INFORMATION | A UI capability or behavior supported by the official nopCommerce demo frontend or official nopCommerce documentation. Documentation can describe configurable platform capability and does not prove that it is enabled in the current demo. |
| OBSERVED BEHAVIOR | Behavior directly exercised and recorded during the live discovery sessions. Observed behavior describes what occurred in the evaluated demo state; it does not automatically establish a universal nopCommerce business rule. |
| PORTFOLIO REQUIREMENT | Expected behavior intentionally defined and approved by the portfolio owner for this clean-room case study. |
| ASSUMPTION | A plausible interpretation that has not been sufficiently verified. |
| OPEN QUESTION / NEEDS CLARIFICATION | Intended behavior is not established and requires manual evidence or an explicit human decision. |

Expected behavior may be established only by an approved portfolio requirement, clearly supported public product behavior, or an explicit human decision. Otherwise, it remains **NEEDS CLARIFICATION**.

The following controls apply:

- Public documentation is not automatically current-demo configuration evidence.
- Public product information is not observed behavior until the portfolio owner verifies it.
- Observation shows what happened, not automatically what should happen.
- An assumption or open question cannot become approved behavior without an explicit human decision.
- Unexpected behavior is not a defect by default. Before requirements are approved, it is classified as **POTENTIAL DEFECT — NEEDS CLARIFICATION** when appropriate.
- This discovery document contains candidate topics, not approved product requirements.

## 3. Environment Constraints

The system under test is the official shared nopCommerce Demo frontend. Other users may change shared state, and the official demo resets periodically.

- Accounts, carts, wishlists, and orders must not be assumed to persist indefinitely.
- Shared catalog or configuration state may change.
- Every execution session must verify relevant preconditions.
- Persistent state created during one session must not automatically become another session's dependency.
- Unexpected behavior should be reproduced before being treated as stable product behavior.
- Session records should capture time, preconditions, state before, state after, and useful evidence references.
- These constraints must influence later test-data and automation architecture decisions, but automation is outside Sprint 1.

## 4. Pre-Discovery Requirement Baseline

> This section preserves the pre-execution understanding, assumptions, candidate state models, and unknowns used to design the discovery run. It is intentionally historical. Current evidence status is maintained in Section 6 — Open Question Register and the reconciled exploratory evidence document.

### 4.1 Authentication

#### 1. What can the user do?

**PUBLIC PRODUCT INFORMATION** indicates that a user can open registration; enter personal, email, password, password-confirmation, and optional UI-exposed information; submit registration; open login; authenticate using email and password; select Remember me; access Forgot password; navigate from login to registration; and encounter a Checkout as Guest option when entering checkout anonymously.

#### 2. What are the preconditions?

- **ASSUMPTION — Registration:** the user is anonymous, has a usable email value, may need a unique email, and populates required fields.
- **ASSUMPTION — Login:** an account exists in current demo state, the reset has not removed it, and supplied credentials correspond to it.
- **ASSUMPTION — Guest checkout:** checkout has been initiated and the cart contains at least one purchasable item.

All candidate preconditions require manual validation.

#### 3. What state changes?

Candidate state models, all **NEEDS CLARIFICATION**, are:

```text
ANONYMOUS → registration submission → REGISTERED
REGISTERED / ANONYMOUS → valid login → AUTHENTICATED SESSION
AUTHENTICATED → logout → ANONYMOUS
ANONYMOUS + CART → checkout → GUEST CHECKOUT
```

#### 4. What behavior is clearly supported?

**PUBLIC PRODUCT INFORMATION** supports the visible existence of registration, required-field indicators, email/password login, Remember me, Forgot password, navigation to registration, and guest-checkout entry. Successful transitions and exact outcomes still require manual observation.

#### 5. What is currently only an assumption?

Password complexity and length; duplicate-email handling; exact validation messages; email verification; CAPTCHA; brute-force protection; account locking; session timeout; Remember me duration; reset persistence; browser-restart behavior; and stale protected-page behavior after logout are **ASSUMPTION** only.

#### 6. What is still unclear?

Exact active registration validation, duplicate-email outcome, configured password rules, invalid-credential behavior, Remember me persistence, protected-page behavior after logout, and reset effects on an existing session remain **NEEDS CLARIFICATION**. See AUTH-OQ-001 through AUTH-OQ-007.

### 4.2 Product Discovery / Search

#### 1. What can the user do?

**PUBLIC PRODUCT INFORMATION** indicates that users can browse top-level and nested categories; perform simple and advanced search; constrain advanced search by category, subcategory, and manufacturer; include descriptions and tags; browse manufacturer and tag pages; switch Grid/List; sort; change page size; and use category, manufacturer, or attribute filters where available.

#### 2. What are the preconditions?

- Search is reachable and the current catalog contains data relevant to the query.
- A category exposes a filter before category filtering can be evaluated.
- Current products and manufacturers exist before manufacturer behavior is evaluated.
- Advanced Search is enabled or opened before advanced controls are used.

These are candidate preconditions; not every category is assumed to expose identical controls.

#### 3. What state changes?

The following candidate models require observation:

```text
DEFAULT PRODUCT LIST → search query → SEARCH RESULT SET
CATEGORY LIST → filter selection → FILTERED RESULT SET
RESULT SET → sort selection → REORDERED RESULT SET
GRID ↔ LIST
PAGE SIZE A → page-size selection → PAGE SIZE B
```

The key investigation is whether the displayed set consistently reflects query, filter, sort, view, and page-size state.

#### 4. What behavior is clearly supported?

**PUBLIC PRODUCT INFORMATION** supports simple search, advanced-search controls, category navigation, sorting, Grid/List, page-size selection, and filtering on applicable pages. Actual controls and combinations remain dependent on live demo configuration and catalog data.

#### 5. What is currently only an assumption?

Case sensitivity; partial, fuzzy, or tokenized matching; relevance rules; filter AND/OR semantics; filter persistence; stable sorting for equal values; zero-result behavior; restoration after clearing filters; stable result counts; discounted-price filtering; and page preservation are **ASSUMPTION** only.

#### 6. What is still unclear?

Keyword matching, combined-filter semantics, sort-related state reset, empty results, old/current-price filter behavior, displayed selling-price sorting, Grid/List preservation, and page-size preservation remain **NEEDS CLARIFICATION**. See DISC-OQ-001 through DISC-OQ-008.

### 4.3 Product Detail & Configuration

#### 1. What can the user do?

**PUBLIC PRODUCT INFORMATION** indicates that a product page may expose name, images, descriptions, manufacturer, SKU, price, tags, quantity, configuration attributes, Add to cart, wishlist, comparison, shipping estimation, related products, and review functionality. Current public evidence indicates that at least one demo product exposes required dimensions such as Size, Color, and Print; different products may expose different configurations.

#### 2. What are the preconditions?

- The product exists and is publicly visible.
- A configurable product may require attribute selection, acceptable quantity, and an available combination.
- A non-configurable product may not require attributes.

These are candidate preconditions and must not be generalized from one product to all products.

#### 3. What state changes?

Potential transitions, all requiring manual confirmation, are:

```text
UNCONFIGURED PRODUCT → select required attributes → CONFIGURED PRODUCT
CONFIGURED PRODUCT → Add to cart → CART UPDATED
PRODUCT → Add to wishlist → WISHLIST UPDATED
PRODUCT → Add to compare → COMPARE LIST UPDATED
PRODUCT PAGE VISIT → potentially RECENTLY VIEWED state
```

#### 4. What behavior is clearly supported?

**PUBLIC PRODUCT INFORMATION** supports configurable products, required attributes on some products, different attribute sets, quantity input, Add to cart, wishlist and comparison actions, related products on some pages, and some interactions restricted by registration state. Each occurrence remains dependent on the selected live product and configuration.

#### 5. What is currently only an assumption?

Incomplete-configuration blocking, exact messages, combination availability, attribute-driven price/SKU/image changes, minimum/maximum/decimal quantity rules, stock behavior, cart merging, separate configuration lines, and refresh persistence are **ASSUMPTION** only.

#### 6. What is still unclear?

Incomplete configuration handling, unavailable combinations, attribute-driven changes, accepted quantity values, invalid/boundary quantities, refresh behavior, and configured-product identity in cart remain **NEEDS CLARIFICATION**. See PDP-OQ-001 through PDP-OQ-007.

### 4.4 Cart

#### 1. What can the user do?

Candidate public or platform behavior includes adding purchasable products, viewing cart contents and item count, changing quantity, removing items, continuing shopping, estimating shipping when enabled, viewing totals, and potentially using discount, gift-card, or terms controls. Each capability must be checked against current demo configuration before it is treated as present.

#### 2. What are the preconditions?

- Add: the product is purchasable and required configuration is complete.
- Update or remove: the cart contains the target item.
- Checkout: the cart contains at least one valid purchasable item.
- Variant-state testing: a configurable product and two distinguishable configurations are available.

These candidate preconditions require live validation.

#### 3. What state changes?

```text
EMPTY CART → add item → ONE-ITEM CART
ONE-ITEM CART → add another product → MULTI-ITEM CART
ONE-ITEM CART → remove → EMPTY CART
MULTI-ITEM CART → remove one → REMAINING ITEMS CART
ITEM QTY = N → update quantity → ITEM QTY = M
CONFIGURATION A + CONFIGURATION B → unknown cart representation
SAME CONFIGURATION + repeated addition → unknown merge/increment/separate outcome
```

The last two transitions are explicit exploration targets and remain **NEEDS CLARIFICATION**.

#### 4. What behavior is clearly supported?

The following behavior requires live verification before classification as observed: header/count after addition, item information, selected configuration representation, quantity and total updates, removal, final-item removal, empty-cart behavior, repeated identical configuration, different configurations of one base product, and header/mini-cart/full-cart synchronization.

#### 5. What is currently only an assumption?

Merge rules; different-attribute line separation; cart persistence across login, reset, or browser restart; guest-cart merging; quantity-zero behavior; equivalence of final-item and multi-item removal; immediate totals; and instant mini/full-cart synchronization are **ASSUMPTION** only.

#### 6. What is still unclear?

Repeated exact configurations, different configuration representation, final-item removal, quantity boundaries, cart-surface synchronization, guest-cart behavior after authentication, reset effects, and configuration price effects remain **NEEDS CLARIFICATION**. See CART-OQ-001 through CART-OQ-008.

### 4.5 Checkout

#### 1. What can the user do?

**PUBLIC PRODUCT INFORMATION** supports guest-checkout entry. The nopCommerce platform supports configurable billing, shipping, payment, and confirmation behavior, but platform capability does not establish the current demo sequence.

#### 2. What are the preconditions?

Likely candidate preconditions are a nonempty valid cart, available checkout action, and valid product configuration. Registered checkout may require authentication; guest checkout likely remains anonymous unless registration is chosen. Additional prerequisites require observation.

#### 3. What state changes?

```text
CART READY → checkout → CHECKOUT STARTED
CHECKOUT STARTED → required information completed → ORDER REVIEW / CONFIRMATION
ORDER CONFIRMED → ORDER CREATED
CART → potentially cleared or changed
REGISTERED ACCOUNT → potentially order visible in history
```

All transitions beyond the supported entry point are **NEEDS CLARIFICATION**.

#### 4. What behavior is clearly supported?

**PUBLIC PRODUCT INFORMATION** supports anonymous checkout initiation and an entry offering Checkout as Guest, Register, and existing-customer login. The detailed flow remains dependent on live demo configuration.

#### 5. What is currently only an assumption?

Exact billing/shipping fields and requirements, methods, terms acceptance, tax, payment processing, order-number format, cart clearing, order persistence, history persistence, and safe completion without external payment are **ASSUMPTION** only.

#### 6. What is still unclear?

The checkout sequence, required fields, shipping appearance and methods, payment methods, safe non-real-payment completion, confirmation state, post-order cart state, and registered-user post-order state remain **NEEDS CLARIFICATION**. See CHK-OQ-001 through CHK-OQ-009.

## 5. Strategic Exploration Probes

These probes are not requirements and not defects. They prioritize state transition, business-rule, boundary/negative, cross-module dependency, and regression-oriented reasoning.

### 5.1 Authentication State

- Compare valid and invalid authentication outcomes.
- Inspect logout and protected-state behavior.
- Inspect stale-session or environment-reset behavior only when safely observable.

### 5.2 Search / Filter Consistency

- Observe query → filter → sort interactions.
- Compare displayed price with price-filter and price-sort behavior.
- Observe empty-result presentation.
- Inspect state preservation after view and page-size changes.

### 5.3 Product Configuration Identity

- Identify required attributes.
- Add different configurations of the same base product.
- Repeat addition of an identical configuration.

### 5.4 Cart State Integrity

- Add an item, update quantity, remove one item, and remove the final item.
- Compare header, mini-cart, and full-cart state.
- Observe duplicate and distinct configuration behavior.

### 5.5 Checkout Dependency

- Compare checkout availability by cart state.
- Inspect guest and authenticated entry choices.
- Observe required-information validation.
- Observe cart/order state after completion only if a safe demo completion is actually executed.

## 6. Open Question Register

| ID | Module | Open Question | Status | Evidence / Current Understanding | Remaining Gap |
|---|---|---|---|---|---|
| AUTH-OQ-001 | Authentication | What exact validation rules are active for registration fields? | NEEDS CLARIFICATION | Standard UI required field indicators observed. | Server-side regex, length boundaries, and localized error messages. |
| AUTH-OQ-002 | Authentication | What happens when an already registered email is submitted? | NEEDS CLARIFICATION | Registration form observed. | Duplicate email submission handling, exact error text, and field value preservation. |
| AUTH-OQ-003 | Authentication | What password rules are currently configured? | NEEDS CLARIFICATION | Password input fields observed. | Minimum/maximum length, character class requirements (uppercase, numbers, symbols), and complexity enforcement. |
| AUTH-OQ-004 | Authentication | What is the observable behavior for invalid credentials? | RESOLVED | Invalid login clears Email (`value=""`) and Password (`value=""`), displays error summary banner `"Login was unsuccessful..."`, user remains anonymous. (Supporting Obs: `OBS-AUTH-006` / `AUTH-EV-004.png`) | None. |
| AUTH-OQ-005 | Authentication | What does Remember me actually persist in this demo? | NEEDS CLARIFICATION | Remember me checkbox exists on login form. | Cookie expiration, session persistence across browser restart, and auth duration. |
| AUTH-OQ-006 | Authentication | What happens to protected account pages after logout? | RESOLVED | Navigating to protected account URLs after logout redirects anonymous user to `/login`. (Supporting Obs: `OBS-AUTH-007`) | None. |
| AUTH-OQ-007 | Authentication | Does the hourly reset invalidate an existing authenticated session immediately, or only remove backing data? | NEEDS CLARIFICATION (ENVIRONMENT-SPECIFIC) | Scheduled backend demo reset occurs hourly. | Session invalidation timing vs database record purge during active session. |
| DISC-OQ-001 | Discovery | How does simple search match keywords: exact, partial, tokenized, or other? | NEEDS CLARIFICATION | Product title keyword matching verified (`build`, `shoes`). | Exact tokenization, stemming, partial string matching, and description index semantics. |
| DISC-OQ-002 | Discovery | How are multiple filters combined? | NEEDS CLARIFICATION | Single manufacturer filter (Nike, `ms=3`) verified. (Supporting Obs: `OBS-DISC-004-FILT` / `DISC-EV-NIKE.png`) | Multi-filter AND/OR combination semantics across multiple attribute dimensions. |
| DISC-OQ-003 | Discovery | What state is reset when sorting changes? | RESOLVED | Changing sort reorders items while preserving active category context. (Supporting Obs: `OBS-DISC-005-SORT`) | None. |
| DISC-OQ-004 | Discovery | What happens when a search produces no result? | RESOLVED | Zero-result search displays `"No products were found that matched your criteria."` empty state message. (Supporting Obs: `OBS-DISC-002`) | None. |
| DISC-OQ-005 | Discovery | How do price filters treat products showing an old price and a current price? | NEEDS CLARIFICATION | Standard product prices observed. | Price range slider inclusion against original list price vs discounted selling price. |
| DISC-OQ-006 | Discovery | Does price sorting use the actual currently displayed selling price? | NEEDS CLARIFICATION | Price low-to-high sorting verified on base catalog products. | Sort rank when attribute configuration alters displayed product price relative to base price. |
| DISC-OQ-007 | Discovery | Does switching Grid/List preserve query, filter, and sort state? | PARTIALLY RESOLVED | Observed: category, active filter (Nike), and sort state preserved while switching Grid/List view. (Supporting Obs: `OBS-DISC-006-VIEW`) | Search-query preservation during Grid/List switching was not tested in this flow. |
| DISC-OQ-008 | Discovery | Does changing page size preserve query, filter, and sort state? | PARTIALLY RESOLVED | Observed: page size updated (`pagesize` parameter), category/filter/sort state preserved. (Supporting Evidence: `Page Size Repair Canonical Record`) | Search-query preservation during page-size change was not tested in this flow. |
| PDP-OQ-001 | Product Detail | What happens when Add to cart is attempted without required attributes? | RESOLVED | Attempting Add to Cart without selecting required options displays top notification warning and blocks addition. (Supporting Obs: `OBS-PDP-004`) | None. |
| PDP-OQ-002 | Product Detail | How does the UI represent unavailable attribute combinations? | NEEDS CLARIFICATION | Valid configuration selections tested. | Visual styling, disabled dropdown options, or submit-time validation for invalid attribute combinations. |
| PDP-OQ-003 | Product Detail | Does selecting different attributes change displayed price, SKU, or image? | PARTIALLY RESOLVED | Displayed price dynamically updates between Config A ($1,315.00), Config B ($1,445.00), and default ($1,200.00). | SKU updates and product main image swaps upon attribute selection not fully evaluated. |
| PDP-OQ-004 | Product Detail | What quantity values are accepted? | PARTIALLY RESOLVED | Apple MacBook Pro PDP exposes a minimum quantity restriction of 2. | Full accepted quantity range, maximum limits, decimal handling, and product-to-product variation. |
| PDP-OQ-005 | Product Detail | What happens with zero, negative, decimal, extremely large, or malformed quantity input? | NEEDS CLARIFICATION | Positive integer quantities (1, 2) tested. | Input sanitization, validation popups, or auto-correction for malformed/extreme quantity values. |
| PDP-OQ-006 | Product Detail | Does refresh preserve or reset selected configuration? | NEEDS CLARIFICATION | Initial attribute selections recorded. | State retention of selected dropdowns/radios upon browser page refresh (F5). |
| PDP-OQ-007 | Product Detail | What uniquely identifies a configured product when it enters the cart? | RESOLVED | Configured products enter cart with distinct attribute summaries appended to product line items. (Supporting Obs: `OBS-PDP-005` / `OBS-CART-002`) | None. |
| CART-OQ-001 | Cart | How is the same exact product configuration handled when added twice? | RESOLVED | Adding an identical product configuration increments the line item quantity (Qty 2 -> 3) on a single row. (Supporting Obs: `OBS-CART-003` / `CART-EV-C3-MICRO.png`) | None. |
| CART-OQ-002 | Cart | How are two different configurations of the same base product represented? | RESOLVED | Different product configurations create distinct cart line rows with separate DOM attribute text summaries. (Supporting Obs: `OBS-CART-004`) | None. |
| CART-OQ-003 | Cart | What happens after the final remaining cart item is removed? | RESOLVED | Removing the final item renders empty cart screen, updates header count to `(0)`, and removes order summary DOM nodes. (Supporting Obs: `OBS-CART-007`) | None. |
| CART-OQ-004 | Cart | What quantity boundaries exist? | NEEDS CLARIFICATION | Quantity updates (1 -> 2 -> 3) verified on shopping cart form. | Maximum line item quantity, maximum cart capacity limit, and high-quantity validation errors. |
| CART-OQ-005 | Cart | How do cart quantity, header count, mini-cart, and full-cart state synchronize? | RESOLVED | Full Cart, Header Count `(N)`, and visible Mini-Cart flyout synchronized consistently across all cart states (C0-C3). (Supporting Evidence: `Cart C0-C3 Canonical Micro-Run`) | None. |
| CART-OQ-006 | Cart | Does guest cart state survive authentication? | NEEDS CLARIFICATION | Guest cart item additions verified. | Guest cart item merge vs overwrite behavior upon logging in with an existing account. |
| CART-OQ-007 | Cart | What happens to the cart when the environment resets? | NEEDS CLARIFICATION (ENVIRONMENT-SPECIFIC) | Active cart state maintained during execution session. | Cart clearance vs retention following backend demo scheduled reset. |
| CART-OQ-008 | Cart | How do configuration price changes affect cart totals? | RESOLVED | Attribute price adjustments dynamically alter item unit price and accurately propagate to subtotal and order totals. (Supporting Obs: `OBS-CART-001` / `OBS-CART-002`) | None. |
| CHK-OQ-001 | Checkout | What is the current checkout step sequence? | RESOLVED | Accordion checkout progresses sequentially: Billing Address -> Shipping Address -> Shipping Method -> Payment Method -> Payment Information -> Confirm Order. (Supporting Obs: `OBS-CHK-004`) | None. |
| CHK-OQ-002 | Checkout | Which billing and address fields are required? | RESOLVED | Observed: live guest-checkout billing form marked First Name, Last Name, Email, Country, City, Address 1, Zip / Postal Code, Phone as required fields. (Supporting Obs: `OBS-CHK-004`) | None for the original question "Which fields are required?". Field-specific negative validation is outside this OQ. |
| CHK-OQ-003 | Checkout | When does shipping information appear? | RESOLVED | In the tested anonymous checkout flow containing a physical product, Shipping Address and Shipping Method appeared after Billing Address and before Payment Method. (Supporting Obs: `OBS-CHK-004`) | None. |
| CHK-OQ-004 | Checkout | Which shipping methods are available in the current demo? | RESOLVED | Guest checkout exposes Ground, Next Day Air, and 2nd Day Air shipping options. (Supporting Obs: `OBS-CHK-004`) | None. |
| CHK-OQ-005 | Checkout | Which payment methods are available? | RESOLVED | Check / Money Order and Credit Card payment options are exposed in payment method step. (Supporting Obs: `OBS-CHK-004`) | None. |
| CHK-OQ-006 | Checkout | Can the demo complete an order without a real monetary transaction? | RESOLVED | Orders can be completed safely using Check / Money Order without external payment gateway processing. (Supporting Obs: `OBS-CHK-005`) | None. |
| CHK-OQ-007 | Checkout | What confirmation state appears after successful order placement? | RESOLVED | Order confirmation renders `"Your order has been successfully processed!"` header and assigns unique order number. (Supporting Obs: `OBS-CHK-005`) | None. |
| CHK-OQ-008 | Checkout | What happens to cart state after successful completion? | RESOLVED | Completing order clears cart, resetting header count to `(0)` and returning cart to empty state. (Supporting Obs: `OBS-CHK-006`) | None. |
| CHK-OQ-009 | Checkout | What additional state is available to registered users after order placement? | NEEDS CLARIFICATION | Guest checkout flow completed and verified. | Order history visibility, PDF invoice download, and re-order functionality in customer account portal. |

## 7. Candidate Requirement Register

These 22 entries are coverage topics, not final requirement wording. None is approved and none has a final requirement ID.

| Candidate | Module | Candidate Topic | Current Evidence Basis | Consolidation Stage |
|---|---|---|---|---|
| CAND-AUTH-01 | Authentication | Registration | PUBLIC PRODUCT INFORMATION + OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-AUTH-02 | Authentication | Authenticated login | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-AUTH-03 | Authentication | Invalid-authentication handling | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-AUTH-04 | Authentication | Guest-checkout entry | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-DISC-01 | Product Discovery | Category navigation | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-DISC-02 | Product Discovery | Simple search | OBSERVED BEHAVIOR | CONSOLIDATE WITH SCOPE LIMITATION |
| CAND-DISC-03 | Product Discovery | Advanced search | OBSERVED BEHAVIOR | CONSOLIDATE WITH SCOPE LIMITATION |
| CAND-DISC-04 | Product Discovery | Applicable product filtering | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-DISC-05 | Product Discovery | Sorting and view-state behavior | OBSERVED BEHAVIOR | CONSOLIDATE WITH SCOPE LIMITATION |
| CAND-PDP-01 | Product Detail | Product information presentation | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-PDP-02 | Product Detail | Required product configuration | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-PDP-03 | Product Detail | Valid configured Add to cart | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-PDP-04 | Product Detail | Quantity and configuration representation | OBSERVED BEHAVIOR | CONSOLIDATE WITH SCOPE LIMITATION |
| CAND-CART-01 | Cart | Added-item representation | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-CART-02 | Cart | Quantity update | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-CART-03 | Cart | Remove an item from cart | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-CART-04 | Cart | Final-item removal and empty-cart state | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-CART-05 | Cart | Configuration identity and repeated additions | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-CHK-01 | Checkout | Checkout entry from nonempty cart | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-CHK-02 | Checkout | Guest, registration, and authenticated entry choices | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-CHK-03 | Checkout | Required checkout information | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |
| CAND-CHK-04 | Checkout | Successful completion and post-order state | OBSERVED BEHAVIOR | READY FOR CONSOLIDATION |

## 8. Discovery Checklist

> This checklist preserves the original discovery actions used to structure the live exploration. The checklist itself is not a PASS/FAIL execution record. Execution outcomes and evidence are maintained in `05-exploratory-notes.md`, where all 44 actions have recorded observations.

For every action, record: precondition, action, actual behavior, state before, state after, useful evidence reference, and uncertainty/open question.

### Authentication

1. Inspect registration fields and required indicators.
2. Register one uniquely identified, disposable, demo-safe test account.
3. Record the actual success behavior.
4. Log out.
5. Log in using the newly created account.
6. Attempt one normal invalid-credential case.
7. Record the actual error behavior.
8. Inspect behavior after logout when navigating back to an account-only page.

### Product Discovery

9. Perform a simple search with a known product keyword.
10. Perform a search expected to return no product.
11. Inspect Advanced Search controls.
12. Use one category constraint.
13. Use one category that exposes product filters.
14. Apply one filter.
15. Change sort order.
16. Switch Grid/List.
17. Change page size where meaningful.
18. Record which state is preserved or reset.

### Product Detail

19. Open one simple or non-configurable product.
20. Open one configurable product.
21. Record required attributes.
22. Attempt Add to cart with an incomplete required configuration.
23. Select a valid configuration.
24. Add the configured product to cart.
25. Record the cart notification, count, and state.

### Cart

26. Inspect the cart-item representation.
27. Change quantity.
28. Add the same exact configuration again.
29. Record whether it merges, increments, or remains separate.
30. Add a different configuration of the same base product if possible.
31. Record how configuration identity is represented.
32. Add another unrelated product.
33. Remove one item from a multi-item cart.
34. Remove the final remaining item.
35. Record the resulting empty-cart state.
36. Observe header, mini-cart, and full-cart synchronization.

### Checkout

37. Prepare a nonempty cart.
38. Start checkout while unauthenticated if practical.
39. Record the guest, registration, and login choices.
40. Enter guest checkout only far enough to discover the actual step sequence.
41. Record required fields and available steps.
42. Do not enter real payment credentials.
43. Complete a demo order only if the site explicitly allows a safe, non-real-payment method.
44. Record post-order state only if actually executed.

Do not create defects during this session. An unexpected result remains **POTENTIAL DEFECT — NEEDS CLARIFICATION** unless expected behavior is already sufficiently established.

## 9. Approved Requirements
