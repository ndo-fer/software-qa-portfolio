# Product Requirement Discovery

## 1. Scope

This document defines the requirement baseline used for the nopCommerce e-commerce case study. It focuses on the flows selected for discovery, test design, execution review, and later regression automation rather than attempting to document every nopCommerce capability.

The primary Sprint 1 product story is:

```text
Authentication
→ Product Discovery / Search
→ Product Detail & Configuration
→ Cart
→ Checkout
```

The intended traceability chain is product evidence → analysis → approved case-study requirement → exploration → scenario and case design → execution → defect and regression reasoning → later automation selection.

The following are future or secondary coverage and are outside the current baseline unless explicitly approved later: custom wishlists, product comparison, product reviews, gift cards, rental products, digital downloads, vendor registration, blog/newsletter, currency switching, email-a-friend, and advanced account management.

## 2. Evidence Policy

| Classification | Meaning |
|---|---|
| PUBLIC PRODUCT INFORMATION | A UI capability or behavior supported by the official nopCommerce demo frontend or official nopCommerce documentation. Documentation can describe configurable platform capability and does not prove that it is enabled in the current demo. |
| OBSERVED BEHAVIOR | Behavior directly exercised and recorded during the live discovery sessions. Observed behavior describes what occurred in the evaluated demo state; it does not automatically establish a universal nopCommerce business rule. |
| CASE-STUDY REQUIREMENT | Expected behavior defined through a documented case-study decision. |
| ASSUMPTION | A plausible interpretation that has not been sufficiently verified. |
| OPEN QUESTION / NEEDS CLARIFICATION | Intended behavior is not established and requires live evidence or an explicit documented decision. |

Expected behavior may be established only by an approved case-study requirement, clearly supported public product behavior, or an explicit documented decision. Otherwise, it remains **NEEDS CLARIFICATION**.

The following controls apply:

- Public documentation is not automatically current-demo configuration evidence.
- Public product information is not observed behavior until it is verified during the case study.
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

> This section preserves the pre-execution understanding, assumptions, candidate state models, and unknowns used to design the discovery run. It is intentionally historical. Current evidence status is maintained in Section 6 — Open Question Register and the exploratory discovery notes.

### 4.1 Authentication

#### 1. What can the user do?

**PUBLIC PRODUCT INFORMATION** indicates that a user can open registration; enter personal, email, password, password-confirmation, and optional UI-exposed information; submit registration; open login; authenticate using email and password; select Remember me; access Forgot password; navigate from login to registration; and encounter a Checkout as Guest option when entering checkout anonymously.

#### 2. What are the preconditions?

- **ASSUMPTION — Registration:** the user is anonymous, has a usable email value, may need a unique email, and populates required fields.
- **ASSUMPTION — Login:** an account exists in current demo state, the reset has not removed it, and supplied credentials correspond to it.
- **ASSUMPTION — Guest checkout:** checkout has been initiated and the cart contains at least one purchasable item.

All candidate preconditions require live validation.

#### 3. What state changes?

Candidate state models, all **NEEDS CLARIFICATION**, are:

```text
ANONYMOUS → registration submission → REGISTERED
REGISTERED / ANONYMOUS → valid login → AUTHENTICATED SESSION
AUTHENTICATED → logout → ANONYMOUS
ANONYMOUS + CART → checkout → GUEST CHECKOUT
```

#### 4. What behavior is clearly supported?

**PUBLIC PRODUCT INFORMATION** supports the visible existence of registration, required-field indicators, email/password login, Remember me, Forgot password, navigation to registration, and guest-checkout entry. Successful transitions and exact outcomes still require direct observation.

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

Potential transitions, all requiring live confirmation, are:

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

## 5. Exploration Focus Areas

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
| DISC-OQ-008 | Discovery | Does changing page size preserve query, filter, and sort state? | PARTIALLY RESOLVED | Observed: page size updated (`pagesize` parameter), category/filter/sort state preserved. (Supporting Observation: `OBS-DISC-007-PAGESIZE`) | Search-query preservation during page-size change was not tested in this flow. |
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
| CART-OQ-005 | Cart | How do cart quantity, header count, mini-cart, and full-cart state synchronize? | RESOLVED | Full Cart, Header Count `(N)`, and visible Mini-Cart flyout synchronized consistently across all cart states (C0-C3). (Supporting Observation: `OBS-CART-005`) | None. |
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

## 7A. Requirement Consolidation Proposal

> Consolidation review completed. The approved case-study baseline is maintained in Section 9.

### 7A.1 Candidate Topic Analysis Summary

| Candidate | Decision | Proposed Requirement Group | Evidence Basis | OQ Dependency | Reasoning |
|---|---|---|---|---|---|
| CAND-AUTH-01 | SPLIT INTO MULTIPLE REQUIREMENTS | REQ-AUTH-001, REQ-AUTH-002 | OBS-AUTH-001, OBS-AUTH-002, OBS-AUTH-003 | OPEN (AUTH-OQ-001, 002, 003) | Form UI accessibility vs registration submission success are separate testable features. Validation rules remain open & scope-limited. |
| CAND-AUTH-02 | KEEP AS ONE REQUIREMENT | REQ-AUTH-003 | OBS-AUTH-005 | OPEN (AUTH-OQ-005) | Valid credential login updates session header. Remember me persistence duration remains open. |
| CAND-AUTH-03 | SPLIT INTO MULTIPLE REQUIREMENTS | REQ-AUTH-004, REQ-AUTH-005 | OBS-AUTH-006, OBS-AUTH-007 | NONE (AUTH-OQ-004, 006 RESOLVED) | Invalid login error/clearing vs protected URL redirect after logout are distinct functional boundaries. |
| CAND-AUTH-04 | MERGE WITH ANOTHER CANDIDATE | Merged into REQ-CHK-001 | OBS-CHK-002 | NONE | Unauthenticated checkout lander entry is part of checkout initiation (CAND-CHK-02). |
| CAND-DISC-01 | KEEP AS ONE REQUIREMENT | REQ-DISC-001 | OBS-DISC-005 | NONE | Standard category navigation renders matching product catalog list. |
| CAND-DISC-02 | SPLIT INTO MULTIPLE REQUIREMENTS | REQ-DISC-002, REQ-DISC-003 | OBS-DISC-001, OBS-DISC-002 | OPEN (DISC-OQ-001), NONE (DISC-OQ-004 RESOLVED) | Keyword search results vs zero-result empty state message are separate outcomes. Matching semantics open under DISC-OQ-001. |
| CAND-DISC-03 | CONSOLIDATE WITH SCOPE LIMITATION | REQ-DISC-004 | OBS-DISC-003, OBS-DISC-004 | OPEN (DISC-OQ-001) | Advanced search category constraint verified; complex boolean logic remains open. |
| CAND-DISC-04 | CONSOLIDATE WITH SCOPE LIMITATION | REQ-DISC-005 | OBS-DISC-004-FILT / DISC-EV-NIKE.png | OPEN (DISC-OQ-002, DISC-OQ-005) | Single manufacturer checkbox filter verified; multi-filter combination semantics remain open. |
| CAND-DISC-05 | SPLIT INTO MULTIPLE REQUIREMENTS | REQ-DISC-006, REQ-DISC-007, REQ-DISC-008 | OBS-DISC-005-SORT, OBS-DISC-006-VIEW, OBS-DISC-007-PAGESIZE | PARTIAL (DISC-OQ-007, DISC-OQ-008), OPEN (DISC-OQ-006) | Sorting, Grid/List view toggle, and page size adjustment are distinct controls. Query preservation during layout changes partially open. |
| CAND-PDP-01 | KEEP AS ONE REQUIREMENT | REQ-PDP-001 | OBS-PDP-001 | NONE | Simple PDP displays basic details, price, SKU, and active cart button without options. |
| CAND-PDP-02 | CONSOLIDATE WITH SCOPE LIMITATION | REQ-PDP-002 | OBS-PDP-002, OBS-PDP-004 | NONE (PDP-OQ-001 RESOLVED), OPEN (PDP-OQ-002) | Missing required configuration blocks cart addition; unavailable combinations open. |
| CAND-PDP-03 | CONSOLIDATE WITH SCOPE LIMITATION | REQ-PDP-003 | OBS-PDP-005, OBS-PDP-006, PDP-EV-001-CONFIGB.png | PARTIAL (PDP-OQ-003), NONE (PDP-OQ-007 RESOLVED) | Price updates dynamically and configured item enters cart; image swap & SKU changes partially open. |
| CAND-PDP-04 | HOLD — INSUFFICIENT EVIDENCE | None (Held) | OBS-PDP-003, PDP-OQ-004 | PARTIAL (PDP-OQ-004), OPEN (PDP-OQ-005, 006) | Quantity boundaries, malformed input handling, and refresh retention are unverified across products. |
| CAND-CART-01 | MERGE WITH ANOTHER CANDIDATE | Merged into REQ-CART-006 | OBS-CART-001, OBS-CART-004 | NONE (PDP-OQ-007, CART-OQ-002 RESOLVED) | Cart line item representation is part of configuration identity (CAND-CART-05). |
| CAND-CART-02 | CONSOLIDATE WITH SCOPE LIMITATION | REQ-CART-001 | OBS-CART-002 | OPEN (CART-OQ-004), NONE (CART-OQ-008 RESOLVED) | Quantity update recalculates totals; max capacity limits open under CART-OQ-004. |
| CAND-CART-03 | KEEP AS ONE REQUIREMENT | REQ-CART-002 | OBS-CART-006 | NONE | Multi-item cart line removal updates table and totals without clearing remaining items. |
| CAND-CART-04 | SPLIT INTO MULTIPLE REQUIREMENTS | REQ-CART-003, REQ-CART-004 | OBS-CART-007, OBS-CART-005 | NONE (CART-OQ-003, CART-OQ-005 RESOLVED) | Final item removal/empty cart screen vs multi-surface (Header/Mini-Cart/Full-Cart) synchronization are distinct concerns. |
| CAND-CART-05 | SPLIT INTO MULTIPLE REQUIREMENTS | REQ-CART-005, REQ-CART-006 | OBS-CART-003, OBS-CART-004, CART-EV-C3-MICRO.png, CART-EV-003.png | NONE (CART-OQ-001, CART-OQ-002 RESOLVED) | Identical configuration quantity merging vs distinct configuration line separation are separate behaviors. |
| CAND-CHK-01 | MERGE WITH ANOTHER CANDIDATE | Merged into REQ-CHK-001 | OBS-CHK-001, OBS-CHK-002 | NONE | Terms acceptance and unauthenticated entry lead into guest checkout lander (CAND-CHK-02). |
| CAND-CHK-02 | CONSOLIDATE WITH SCOPE LIMITATION | REQ-CHK-001 | OBS-CHK-002, OBS-CHK-003 | NONE (CHK-OQ-001 RESOLVED) | Unauthenticated checkout lander presents Guest/Register/Login options and initiates guest checkout flow. |
| CAND-CHK-03 | SPLIT INTO MULTIPLE REQUIREMENTS | REQ-CHK-002, REQ-CHK-003 | OBS-CHK-004, OBS-CHK-005 | NONE (CHK-OQ-001, 002, 003, 004, 005 RESOLVED) | Step sequence & required billing fields vs shipping/payment option selection are distinct checkout stages. |
| CAND-CHK-04 | SPLIT INTO MULTIPLE REQUIREMENTS | REQ-CHK-004, REQ-CHK-005 | OBS-CHK-005, OBS-CHK-006 | NONE (CHK-OQ-006, 007, 008 RESOLVED), OPEN (CHK-OQ-009) | Order confirmation page display vs post-order cart reset are distinct outcomes. Registered user history open under CHK-OQ-009. |

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

### 9.1 Authentication Module

- **Requirement ID:** REQ-AUTH-001
  - **Module:** Authentication
  - **Title:** Registration Form Accessibility & Required Field Indicators
  - **Precondition:** Storefront header is accessible to an anonymous user.
  - **Requirement:** When an anonymous user clicks the "Register" link in the header, the storefront shall display the registration form containing personal data fields (Gender, First name, Last name, Date of birth, Email, Company details) with mandatory input fields marked with visual indicators (`*`).
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-AUTH-001` / `AUTH-EV-001.png`
  - **Scope Limitation:** Client-side tooltips, field layout responsiveness, and visual styling are strictly bounded to current demo layout. Server-side regex and exact field length limits remain unverified.
  - **Dependent Open Questions:** `AUTH-OQ-001`, `AUTH-OQ-003`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-AUTH-002
  - **Module:** Authentication
  - **Title:** Successful User Account Registration
  - **Precondition:** User is on the registration page with valid, unique user registration details.
  - **Requirement:** When a user fills all required fields with valid, non-duplicate registration data and clicks "Register", the storefront shall create the account and render the confirmation message `"Your registration completed"`.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-AUTH-002`, `OBS-AUTH-003` / `AUTH-EV-002.png`, `AUTH-EV-003.png`
  - **Scope Limitation:** Registration success is bounded to unique disposable email addresses. Duplicate email submission outcomes and server-side validation error messages remain unverified.
  - **Dependent Open Questions:** `AUTH-OQ-001`, `AUTH-OQ-002`, `AUTH-OQ-003`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-AUTH-003
  - **Module:** Authentication
  - **Title:** Successful Authentication and Session Header State
  - **Precondition:** Account exists in the current environment and user is on the login page.
  - **Requirement:** When a user enters valid registered credentials (Email and Password) and clicks "Log in", the storefront shall authenticate the session and update the header navigation to display the customer account link and a "Log out" action.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-AUTH-005`
  - **Scope Limitation:** Remember me persistence across browser restarts and session duration remain unverified.
  - **Dependent Open Questions:** `AUTH-OQ-005`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-AUTH-004
  - **Module:** Authentication
  - **Title:** Invalid Login Credential Handling & Field Clearing
  - **Precondition:** User is on the login page.
  - **Requirement:** When a user submits invalid or unrecognized login credentials, the storefront shall reject authentication, remain in anonymous state, display an error summary banner containing `"Login was unsuccessful..."`, and clear both the Email and Password input fields (`value=""`).
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-AUTH-006` / `AUTH-EV-004.png`
  - **Scope Limitation:** Bounded to single invalid login attempt. Account locking, attempt limits, and brute-force throttling remain unverified.
  - **Dependent Open Questions:** NONE (`AUTH-OQ-004` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-AUTH-005
  - **Module:** Authentication
  - **Title:** Protected Page Access Redirection for Anonymous Users
  - **Precondition:** User is currently anonymous (unauthenticated or logged out).
  - **Requirement:** When an anonymous user attempts direct URL navigation to a protected customer account URL (e.g., `/customer/info`), the storefront shall block access and redirect the browser to `/login`.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-AUTH-007`
  - **Scope Limitation:** Evaluated for customer info URL only; other protected admin or account endpoints remain unverified.
  - **Dependent Open Questions:** NONE (`AUTH-OQ-006` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

### 9.2 Product Discovery / Search Module

- **Requirement ID:** REQ-DISC-001
  - **Module:** Product Discovery
  - **Title:** Category Catalog Navigation
  - **Precondition:** Storefront navigation menu is visible.
  - **Requirement:** When a user clicks a top-level or sub-category link in the catalog menu (e.g., `/shoes` or `/computers`), the storefront shall display the category page containing the category title, breadcrumb trail, and the list of assigned products.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-DISC-005` / `DISC-EV-001.png`
  - **Scope Limitation:** Bounded to active categories in demo catalog.
  - **Dependent Open Questions:** NONE
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-DISC-002
  - **Module:** Product Discovery
  - **Title:** Simple Search Execution & Keyword Matching
  - **Precondition:** Search input bar is visible in storefront header.
  - **Requirement:** When a user enters a product title keyword (e.g., `"computer"`) and submits the search form, the storefront shall return a product listing page containing products matching the query keyword.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-DISC-001`
  - **Scope Limitation:** Matching algorithm tokenization, stemming, description indexing, and fuzzy matching rules remain unverified.
  - **Dependent Open Questions:** `DISC-OQ-001`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-DISC-003
  - **Module:** Product Discovery
  - **Title:** Zero-Result Search Empty State Display
  - **Precondition:** User submits a search query that matches zero items in the catalog.
  - **Requirement:** When a search query yields no catalog matches, the storefront shall render an empty state message displaying `"No products were found that matched your criteria."`.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-DISC-002` / `DISC-EV-002.png`
  - **Scope Limitation:** Bounded to standard simple search submit.
  - **Dependent Open Questions:** NONE (`DISC-OQ-004` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-DISC-004
  - **Module:** Product Discovery
  - **Title:** Advanced Search Category and Subcategory Filtering
  - **Precondition:** User is on the Advanced Search page (`/search`).
  - **Requirement:** When a user enters a search term, selects a specific Category constraint, enables "Automatically search sub categories", and submits the form, the storefront shall return only products matching both the query keyword and the selected category hierarchy.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-DISC-003`, `OBS-DISC-004` / `DISC-EV-003.png`, `DISC-EV-004.png`
  - **Scope Limitation:** Multi-category selection and price-range advanced search parameters remain unverified.
  - **Dependent Open Questions:** `DISC-OQ-001`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-DISC-005
  - **Module:** Product Discovery
  - **Title:** Manufacturer Filtering
  - **Precondition:** User is viewing a category page that exposes specification filters (e.g., `/shoes`).
  - **Requirement:** When a user selects a manufacturer checkbox filter (e.g., `Nike`), the storefront shall update the displayed product list to include only products matching the selected specification option.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-DISC-004-FILT` / `DISC-EV-NIKE.png`
  - **Scope Limitation:** Multi-filter boolean AND/OR combinations and price slider interactions remain unverified.
  - **Dependent Open Questions:** `DISC-OQ-002`, `DISC-OQ-005`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-DISC-006
  - **Module:** Product Discovery
  - **Title:** Catalog Product Sorting and Category Preservation
  - **Precondition:** User is viewing a product listing page.
  - **Requirement:** When a user selects a sort option from the "Sort by" dropdown (e.g., `Price: Low to High`), the storefront shall reorder the displayed product set according to the selected criteria while maintaining the active category context.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-DISC-005-SORT`
  - **Scope Limitation:** Displayed selling price vs base price sorting on configurable products remains unverified.
  - **Dependent Open Questions:** `DISC-OQ-006`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-DISC-007
  - **Module:** Product Discovery
  - **Title:** View Mode Layout Switching and Filter/Sort State Retention
  - **Precondition:** User is viewing a product listing page with active filter or sort options.
  - **Requirement:** When a user toggles the view mode control between Grid and List view, the storefront shall adjust the product item DOM layout while preserving active category, manufacturer filter, and sort state.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-DISC-006-VIEW`
  - **Scope Limitation:** Preservation of active simple search query strings across view toggles was not tested and remains unverified.
  - **Dependent Open Questions:** `DISC-OQ-007` (PARTIALLY RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-DISC-008
  - **Module:** Product Discovery
  - **Title:** Page Size Adjustment and State Preservation
  - **Precondition:** User is viewing a category or product listing page exposing page size options.
  - **Requirement:** When a user selects a different page size option (e.g., changing dropdown from 6 to 3), the storefront shall adjust the visible product count per page, append `pagesize=N` to the URL, and preserve active category, filter, and sort state.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-DISC-007-PAGESIZE`
  - **Scope Limitation:** Preservation of active simple search query strings across page size adjustments was not tested and remains unverified.
  - **Dependent Open Questions:** `DISC-OQ-008` (PARTIALLY RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

### 9.3 Product Detail & Configuration Module

- **Requirement ID:** REQ-PDP-001
  - **Module:** Product Detail
  - **Title:** Simple Non-Configurable Product Information Display
  - **Precondition:** User opens the detail page of a simple product (e.g., `Digital Storm VANQUISH Custom Performance PC`).
  - **Requirement:** The storefront shall display product title, SKU, price (`$1,259.00`), quantity input, and an active "Add to cart" button without requiring mandatory option selections.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-PDP-001` / `PDP-EV-001.png`
  - **Scope Limitation:** Bounded to non-configurable simple product pages.
  - **Dependent Open Questions:** NONE
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-PDP-002
  - **Module:** Product Detail
  - **Title:** Required Attribute Configuration Enforcement
  - **Precondition:** User is viewing a PDP for a configurable product requiring mandatory attribute selections (e.g., `Build your own computer`).
  - **Requirement:** When a user clicks "Add to cart" without selecting all mandatory attribute options, the storefront shall block cart addition and display a top notification error message.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-PDP-002`, `OBS-PDP-004` / `PDP-EV-002.png`
  - **Scope Limitation:** Out-of-stock or incompatible option combination handling remains unverified.
  - **Dependent Open Questions:** NONE (`PDP-OQ-001` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-PDP-003
  - **Module:** Product Detail
  - **Title:** Dynamic Price Update and Configured Cart Addition
  - **Precondition:** User is viewing a configurable product PDP with option pricing adjustments.
  - **Requirement:** When a user selects attribute options with price surcharges (e.g., Config A or Config B), the storefront shall dynamically update the displayed product price, and clicking "Add to cart" shall add the configured item to cart, render a top green confirmation bar, and increment the header cart count.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-PDP-005`, `OBS-PDP-006`, `PDP-EV-001-CONFIGB.png`
  - **Scope Limitation:** Image thumbnail swapping and SKU code changes upon attribute selection remain unverified.
  - **Dependent Open Questions:** `PDP-OQ-003` (PARTIALLY RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

### 9.4 Cart Module

- **Requirement ID:** REQ-CART-001
  - **Module:** Cart
  - **Title:** Cart Line Item Quantity Update and Subtotal Recalculation
  - **Precondition:** Shopping cart contains an item.
  - **Requirement:** When a user modifies the quantity input field for a cart line item (e.g., 1 -> 2) and clicks "Update shopping cart", the storefront shall recalculate and update the line item subtotal and overall cart total.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CART-002` / `CART-EV-002.png`
  - **Scope Limitation:** Maximum quantity boundaries, stock limit validation error popups, and high-quantity input sanitization remain unverified.
  - **Dependent Open Questions:** `CART-OQ-004`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CART-002
  - **Module:** Cart
  - **Title:** Multi-Item Cart Line Item Removal
  - **Precondition:** Shopping cart contains two or more distinct line item rows.
  - **Requirement:** When a user selects the "Remove" control for one line item in a multi-item cart, the storefront shall remove that line item from the cart table, update the header count badge, and recalculate cart totals while retaining all remaining cart items.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CART-006` / `CART-EV-004.png`
  - **Scope Limitation:** Bounded to multi-item cart state.
  - **Dependent Open Questions:** NONE
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CART-003
  - **Module:** Cart
  - **Title:** Final Cart Item Removal and Empty Cart State
  - **Precondition:** Shopping cart contains exactly one line item.
  - **Requirement:** When a user removes the final item from the shopping cart, the storefront shall transition to empty cart state, display `"Your Shopping Cart is empty!"`, reset header cart count to `(0)`, and hide order summary and checkout action buttons.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CART-007`
  - **Scope Limitation:** Bounded to final item removal.
  - **Dependent Open Questions:** NONE (`CART-OQ-003` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CART-004
  - **Module:** Cart
  - **Title:** Cart Surface State Synchronization across Full Cart, Header, and Mini-Cart
  - **Precondition:** Cart state transitions occur (addition, quantity update, removal).
  - **Requirement:** The storefront shall maintain immediate state synchronization between the header cart count badge `(N)`, the mini-cart flyout dropdown, and the full shopping cart table across all cart states (C0 through C3).
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CART-005`
  - **Scope Limitation:** Bounded to active browser session interactions. Guest cart merging upon authentication remains unverified.
  - **Dependent Open Questions:** NONE (`CART-OQ-005` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CART-005
  - **Module:** Cart
  - **Title:** Identical Product Configuration Quantity Merging
  - **Precondition:** Shopping cart contains a configured product, and user adds the identical product configuration again from the PDP.
  - **Requirement:** When an identical product configuration is added to cart a second time, the storefront shall merge the addition into the existing line item row by incrementing its quantity (e.g., Qty 2 -> 3) rather than creating a duplicate row.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CART-003` / `CART-EV-C3-MICRO.png`
  - **Scope Limitation:** Bounded to exact matching attribute configurations.
  - **Dependent Open Questions:** NONE (`CART-OQ-001` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CART-006
  - **Module:** Cart
  - **Title:** Distinct Product Configuration Line Item Separation
  - **Precondition:** Shopping cart contains a configured product, and user adds a different configuration of the same base product from the PDP.
  - **Requirement:** When a different configuration of an existing base product is added to cart, the storefront shall create a separate cart line item row displaying its specific attribute option summary text.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CART-004` / `CART-EV-003.png`
  - **Scope Limitation:** Bounded to distinguishable attribute configurations.
  - **Dependent Open Questions:** NONE (`CART-OQ-002` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

### 9.5 Checkout Module

- **Requirement ID:** REQ-CHK-001
  - **Module:** Checkout
  - **Title:** Anonymous Checkout Initiation and Guest Entry
  - **Precondition:** Anonymous user has a nonempty cart and accepts the Terms of Service checkbox on `/cart`.
  - **Requirement:** When an anonymous user clicks "Checkout", the storefront shall display the checkout lander page offering "Checkout as Guest", "Register", and "Returning Customer / Login" options, and clicking "Checkout as Guest" shall initiate the guest checkout process.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CHK-001`, `OBS-CHK-002`, `OBS-CHK-003` / `CHK-EV-001.png`, `CHK-EV-002.png`
  - **Scope Limitation:** Bounded to anonymous physical-product checkout initiation.
  - **Dependent Open Questions:** NONE (`CHK-OQ-001` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CHK-002
  - **Module:** Checkout
  - **Title:** Guest Checkout Step Sequence and Required Billing Fields
  - **Precondition:** User initiates guest checkout for a physical product.
  - **Requirement:** The storefront shall present the tested guest checkout sequence as Billing Address -> Shipping Address -> Shipping Method -> Payment Method -> Payment Information -> Confirm Order, and shall mark First Name, Last Name, Email, Country, City, Address 1, Zip/Postal Code, and Phone as required billing fields.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CHK-004` / `CHK-EV-003.png`
  - **Scope Limitation:** Negative field-level inline validation rules remain unverified.
  - **Dependent Open Questions:** NONE (`CHK-OQ-001`, `CHK-OQ-002` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CHK-003
  - **Module:** Checkout
  - **Title:** Shipping and Payment Method Selection in Guest Checkout
  - **Precondition:** User is in the guest checkout accordion sequence.
  - **Requirement:** The storefront shall expose shipping method options (Ground, Next Day Air, 2nd Day Air) after shipping address confirmation, and payment method options (Check / Money Order, Credit Card) prior to order review.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CHK-004`, `OBS-CHK-005` / `CHK-EV-004.png`
  - **Scope Limitation:** Credit card payment gateway authorization and processing remain unverified.
  - **Dependent Open Questions:** NONE (`CHK-OQ-004`, `CHK-OQ-005` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CHK-004
  - **Module:** Checkout
  - **Title:** Demo Order Completion and Confirmation Display
  - **Precondition:** User selects Check / Money Order payment method and reaches the Confirm Order step.
  - **Requirement:** When the user submits order confirmation, the storefront shall process the order without requiring external payment gateway processing, render `"Your order has been successfully processed!"`, and assign a unique order number.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CHK-005` / `CHK-EV-005.png`
  - **Scope Limitation:** Registered user account portal order history, PDF invoice generation, and re-order functionality remain unverified.
  - **Dependent Open Questions:** `CHK-OQ-009`
  - **Status:** APPROVED — CASE-STUDY BASELINE

- **Requirement ID:** REQ-CHK-005
  - **Module:** Checkout
  - **Title:** Post-Order Cart Reset to Empty State
  - **Precondition:** Order confirmation is successfully processed.
  - **Requirement:** Upon order completion confirmation, the storefront shall clear the active shopping cart, reset line item count to 0, and restore header cart count to `(0)`.
  - **Evidence Basis:** OBSERVED BEHAVIOR
  - **Supporting Observation / Evidence:** `OBS-CHK-006`
  - **Scope Limitation:** Bounded to guest checkout session completion.
  - **Dependent Open Questions:** NONE (`CHK-OQ-008` RESOLVED)
  - **Status:** APPROVED — CASE-STUDY BASELINE
