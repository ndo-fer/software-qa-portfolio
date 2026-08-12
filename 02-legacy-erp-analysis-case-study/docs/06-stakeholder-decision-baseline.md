# Stakeholder Decision Baseline

## Purpose and Interpretation

This baseline records synthetic stakeholder decisions for the fictional Northstar Components Manufacturing V1 release. The 15 selected questions are the minimum high-impact set chosen to support a coherent requirement baseline across Purchasing, Sales, Inventory, Manufacturing, permissions, and inventory traceability.

These decisions are intentionally defined **fictional case decisions**. They are not observed legacy behavior, employer requirements, industry-standard requirements, or evidence about a real application. Questions not listed here remain open unless a V1 boundary explicitly leaves the related capability out of scope.

| OQ ID | Synthetic Stakeholder Decision | Rationale | Affected Capability | Status |
|---|---|---|---|---|
| OQ-PUR-001 | Every standard inventory Purchase Order in V1 must originate from an approved Purchase Request. Emergency-purchase exceptions are outside V1. | Establishes one traceable entry path without introducing exception workflows. | LEG-PUR-001, LEG-PUR-002 | DECIDED FOR FICTIONAL V1 |
| OQ-PUR-002 | Partial Goods Receipts are allowed. The unreceived quantity remains outstanding on the Purchase Order line. | Supports ordinary split supplier deliveries while preserving the remaining commitment. | LEG-PUR-002, LEG-PUR-003 | DECIDED FOR FICTIONAL V1 |
| OQ-PUR-003 | A Goods Receipt quantity greater than the Purchase Order line's remaining quantity is blocked. V1 has no over-receipt tolerance. | Provides an unambiguous control and avoids unsupported tolerance rules. | LEG-PUR-003 | DECIDED FOR FICTIONAL V1 |
| OQ-PUR-004 | A partially received Purchase Order remains `PARTIALLY RECEIVED` until all remaining quantities are received or an authorized user explicitly closes the remainder. | Makes outstanding commitments and terminal states visible. | LEG-PUR-002, LEG-PUR-006 | DECIDED FOR FICTIONAL V1 |
| OQ-SAL-001 | Confirming a Sales Order reserves only the currently available quantity. Any unreserved balance remains unallocated; V1 does not automate replenishment or backorder orchestration. | Prevents over-reservation while preserving visibility of unmet demand. | LEG-SAL-001, LEG-INV-001, LEG-INV-006 | DECIDED FOR FICTIONAL V1 |
| OQ-SAL-002 | Partial delivery is allowed. Undelivered quantity remains outstanding, and the Sales Order remains `PARTIALLY DELIVERED` until fully delivered. | Supports split fulfillment with explicit remaining quantities. | LEG-SAL-001, LEG-SAL-002, LEG-SAL-005 | DECIDED FOR FICTIONAL V1 |
| OQ-SAL-004 | Rules for inspecting and returning customer goods to available stock are not defined in V1. Sales-return processing is deferred. | A reliable return workflow requires disposition and inspection decisions not needed for the selected first-release flows. | LEG-SAL-003 | DEFERRED |
| OQ-INV-001 | Posting a Goods Receipt increases on-hand inventory by the posted quantity. A draft or unposted receipt does not change on-hand inventory. | Defines the exact inventory event without vague timing language. | LEG-PUR-003, LEG-INV-001, LEG-INV-002 | DECIDED FOR FICTIONAL V1 |
| OQ-INV-002 | Posting a stock adjustment that would reduce resulting on-hand quantity below zero is blocked. | Establishes a clear V1 inventory-integrity boundary. | LEG-INV-001, LEG-INV-004 | DECIDED FOR FICTIONAL V1 |
| OQ-INV-004 | An inter-warehouse transfer follows `DRAFT` → `DISPATCHED / IN TRANSIT` → `RECEIVED`. Source on-hand decreases at dispatch; destination on-hand increases at receipt. | Separates custody changes and makes stock in transit observable. | LEG-INV-001, LEG-INV-002, LEG-INV-003 | DECIDED FOR FICTIONAL V1 |
| OQ-MFG-001 | Components are deducted from on-hand inventory when actual material consumption is posted. Recording an unposted consumption entry does not change stock. | Defines a single observable posting event for component usage. | LEG-MFG-003, LEG-MFG-004, LEG-INV-001 | DECIDED FOR FICTIONAL V1 |
| OQ-MFG-003 | V1 blocks posted production output greater than the Production Order's remaining planned quantity. A future capability for approved overproduction or tolerance is deferred. | Creates a testable V1 limit while keeping tolerance governance outside scope. | LEG-MFG-003, LEG-MFG-006 | DECIDED FOR FICTIONAL V1 |
| OQ-MFG-004 | Posting a Production Result increases finished-item on-hand inventory. When cumulative posted output reaches the planned quantity, the Production Order becomes `COMPLETED`. | Defines when production output becomes inventory and when the order reaches its terminal V1 state. | LEG-MFG-003, LEG-MFG-005, LEG-MFG-006, LEG-INV-001 | DECIDED FOR FICTIONAL V1 |
| OQ-SYS-001 | V1 uses fixed role-based permissions for `create`, `approve`, `post`, and `cancel`. The applicable role must hold the permission for the attempted action; no dynamic policy engine is included. | Establishes simple, testable authorization boundaries across modules. | LEG-MST-006 and controlled transaction capabilities | DECIDED FOR FICTIONAL V1 |
| OQ-SYS-004 | Every posted quantity-changing transaction retains source document ID, transaction type, timestamp, responsible user, quantity change, affected item, and source or destination location when relevant. | Provides a consistent minimum inventory audit trail across operational flows. | LEG-INV-002 and all quantity-changing capabilities | DECIDED FOR FICTIONAL V1 |

## Decisions Left Outside the V1 Baseline

- OQ-INV-003 is not separately resolved. Stock-adjustment actions use the fixed role permissions established by OQ-SYS-001; advanced separation-of-duties rules are not introduced.
- OQ-MFG-002 remains outside the V1 requirement baseline. V1 records actual consumption and the difference from the applicable Bill of Materials quantity, but does not define tolerance tiers or variance-authorization governance.
- OQ-SYS-002 and OQ-SYS-003 remain open because contextual approval matrices and master-data approval/effective dating are outside this compact baseline.
