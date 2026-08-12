# Legacy-to-Web Mapping

Every decision below is a preliminary **analyst proposal** for the fictional target system. It is not a confirmed historical fact, approved requirement, or employer decision. Confidence reflects the strength of the proposal based only on this clean-room working model; it does not indicate that the underlying business rule has been validated.

Decision meanings used here:

- **RETAIN:** preserve the business capability, while normal web implementation changes remain possible.
- **REDESIGN:** preserve the business intent but materially revise interaction, control, or process structure.
- **MERGE:** combine related legacy concepts or views into a coherent target capability.
- **REPLACE:** satisfy the intent through a different standard capability.
- **DEPRECATE:** omit a capability that no longer provides justified business value.
- **NEEDS CLARIFICATION:** defer a direction because a material business decision is unresolved.

The taxonomy is not a distribution target. Categories with no justified entries are intentionally unused.

| Legacy ID | Capability | Proposed Web Capability | Decision | Rationale | Confidence |
|---|---|---|---|---|---|
| LEG-MST-001 | Product / Material Records | Unified Item Master with controlled item types | MERGE | A shared model could reduce duplicate maintenance while distinguishing raw materials, intermediates, and finished goods. | MEDIUM |
| LEG-MST-002 | Supplier Records | Supplier Master | RETAIN | Supplier identity and operational contact data remain necessary for purchasing. | HIGH |
| LEG-MST-003 | Customer Records | Customer Master | RETAIN | Customer and delivery data remain necessary for sales fulfillment. | HIGH |
| LEG-MST-004 | Warehouse / Location Records | Hierarchical Warehouse and Location Management | REDESIGN | A browser-based hierarchy could make storage structure and transaction selection clearer. | MEDIUM |
| LEG-MST-005 | Units of Measure | Unit-of-Measure Master | RETAIN | Consistent quantity units are a foundational cross-module capability. | HIGH |
| LEG-MST-006 | Users / Permissions | Role-Based Access and Approval Management | REDESIGN | Roles and explicit permissions better express functional access and approval authority than isolated user settings. | HIGH |
| LEG-PUR-001 | Purchase Request | Web Purchase Request Workflow | REDESIGN | A visible status and approval path could make internal demand traceable; mandatory use remains unresolved. | MEDIUM |
| LEG-PUR-002 | Purchase Order | Controlled Purchase Order Workflow | REDESIGN | The business commitment remains, but status, approval, revision, and cancellation controls need explicit design. | HIGH |
| LEG-PUR-003 | Goods Receipt | Purchase Receipt Processing | REDESIGN | Receipt entry should connect ordered, received, and outstanding quantities with a defined stock-posting event. | MEDIUM |
| LEG-PUR-004 | Purchase Return | Supplier Return Workflow | REDESIGN | Returns need traceability to received goods and an explicit inventory effect. | MEDIUM |
| LEG-PUR-005 | Supplier Quotation Comparison | Sourcing and Supplier Comparison Workspace | MERGE | Supplier offers and comparisons can be evaluated in one sourcing context instead of separate views. | LOW |
| LEG-PUR-006 | Purchase Status Inquiry | Request-to-Receipt Tracking Workspace | REDESIGN | A consolidated timeline could replace fragmented inquiry navigation without changing the underlying transactions. | HIGH |
| LEG-SAL-001 | Sales Order | Controlled Sales Order Workflow | REDESIGN | Order acceptance, stock checks, reservation, changes, and cancellation require an explicit web process. | HIGH |
| LEG-SAL-002 | Delivery | Sales Fulfillment and Delivery Processing | REDESIGN | Fulfillment should show ordered, allocated, delivered, and remaining quantities with a defined stock event. | MEDIUM |
| LEG-SAL-003 | Sales Return | Customer Return and Disposition Workflow | REDESIGN | Returned goods need receipt, inspection or disposition visibility before reusable stock is assumed. | MEDIUM |
| LEG-SAL-004 | Customer Price Reference | Target Pricing Capability | NEEDS CLARIFICATION | The case does not establish whether pricing is maintained, calculated, negotiated, or externally governed. | LOW |
| LEG-SAL-005 | Sales Status Inquiry | Order-to-Delivery Tracking Workspace | MERGE | Order and delivery progress can be presented as one fulfillment view while retaining source transactions. | HIGH |
| LEG-INV-001 | Stock Position | Real-Time Stock Position View | RETAIN | Users still need quantities by item and storage point; which quantity states appear remains open. | HIGH |
| LEG-INV-002 | Stock Movement History | Inventory Transaction History | RETAIN | Traceable quantity-changing events remain essential across operational modules. | HIGH |
| LEG-INV-003 | Warehouse Transfer | Controlled Stock Transfer Workflow | REDESIGN | The target should make source, destination, transit, dispatch, and receipt states explicit as needed. | MEDIUM |
| LEG-INV-004 | Stock Adjustment | Authorized Inventory Correction Workflow | REDESIGN | Reason, responsibility, approval, and posting controls should be visible and auditable. | HIGH |
| LEG-INV-005 | Stock Opname | Physical Count and Variance Workflow | REDESIGN | Separate counting, variance review, and posting stages could reduce ambiguity and improve control. | MEDIUM |
| LEG-INV-006 | Inventory Reservation | Inventory Reservation Capability | NEEDS CLARIFICATION | The case has not established eligible demand, priority rules, release conditions, or quantity semantics. | LOW |
| LEG-INV-007 | Lot / Batch Reference | Selective Lot and Batch Traceability | NEEDS CLARIFICATION | Traceability scope depends on item classes and business or regulatory needs not yet defined. | LOW |
| LEG-MFG-001 | Bill of Materials | Bill of Materials Management | RETAIN | Component structure remains central to manufacturing, although versioning controls require later definition. | HIGH |
| LEG-MFG-002 | Production Planning | Web Production Planning Workspace | REDESIGN | Planning should expose demand, timing, and status clearly while avoiding unsupported advanced forecasting. | MEDIUM |
| LEG-MFG-003 | Production Order / Work Order | Controlled Production Order Workflow | REDESIGN | Release, execution, change, cancellation, and closure need explicit states and authority. | HIGH |
| LEG-MFG-004 | Material Consumption | Production Material-Issue Capability | NEEDS CLARIFICATION | The posting method cannot be selected until issue timing, actual usage, and backflush expectations are defined. | LOW |
| LEG-MFG-005 | Production Execution Status | Production Progress Tracking | REDESIGN | A concise milestone view could provide visibility without reproducing fragmented desktop steps. | MEDIUM |
| LEG-MFG-006 | Production Result | Production Output Receipt | REDESIGN | Output entry should connect planned and actual quantities to a defined inventory-availability event. | MEDIUM |
