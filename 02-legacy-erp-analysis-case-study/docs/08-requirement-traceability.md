# Requirement Traceability

## Traceability Matrix

This matrix links every fictional V1 functional requirement to its governing business rules, selected synthetic stakeholder decisions, and Sprint 1 legacy capabilities. A requirement may map to multiple sources where behavior crosses module boundaries. There are no requirements derived from external ERP defaults or private source material.

| Requirement | Business Rule | Stakeholder Decision / OQ | Legacy Capability | Target Module |
|---|---|---|---|---|
| FR-PUR-001 | BR-SYS-001 | OQ-PUR-001 | LEG-PUR-001, LEG-PUR-002 | Purchasing |
| FR-PUR-002 | BR-PUR-001, BR-PUR-002, BR-INV-003, BR-SYS-001 | OQ-PUR-002, OQ-INV-001, OQ-SYS-004 | LEG-PUR-002, LEG-PUR-003, LEG-INV-001, LEG-INV-002 | Purchasing / Inventory |
| FR-PUR-003 | BR-PUR-001 | OQ-PUR-003 | LEG-PUR-003 | Purchasing |
| FR-PUR-004 | BR-PUR-002, BR-SYS-001 | OQ-PUR-004, OQ-SYS-001 | LEG-PUR-002, LEG-PUR-006 | Purchasing |
| FR-SAL-001 | BR-SAL-001, BR-SYS-001 | OQ-SAL-001, OQ-SYS-001 | LEG-SAL-001, LEG-INV-001, LEG-INV-006 | Sales / Inventory |
| FR-SAL-002 | BR-SAL-002, BR-SAL-003, BR-INV-003, BR-SYS-001 | OQ-SAL-002, OQ-SYS-004 | LEG-SAL-001, LEG-SAL-002, LEG-INV-001, LEG-INV-002, LEG-INV-006 | Sales / Inventory |
| FR-SAL-003 | BR-SAL-002, BR-SAL-003 | OQ-SAL-001, OQ-SAL-002 | LEG-SAL-001, LEG-SAL-002, LEG-INV-006 | Sales / Inventory |
| FR-SAL-004 | BR-SAL-001, BR-SAL-002 | OQ-SAL-001, OQ-SAL-002 | LEG-SAL-001, LEG-SAL-005, LEG-INV-006 | Sales |
| FR-INV-001 | BR-PUR-002, BR-INV-003 | OQ-INV-001, OQ-SYS-004 | LEG-PUR-003, LEG-INV-001, LEG-INV-002 | Inventory |
| FR-INV-002 | BR-INV-001, BR-INV-003, BR-SYS-001 | OQ-INV-002, OQ-SYS-001, OQ-SYS-004 | LEG-INV-001, LEG-INV-002, LEG-INV-004 | Inventory |
| FR-INV-003 | BR-INV-001 | OQ-INV-002 | LEG-INV-001, LEG-INV-004 | Inventory |
| FR-INV-004 | BR-INV-002, BR-INV-003, BR-SYS-001 | OQ-INV-004, OQ-SYS-001, OQ-SYS-004 | LEG-INV-001, LEG-INV-002, LEG-INV-003 | Inventory |
| FR-INV-005 | BR-INV-002, BR-INV-003, BR-SYS-001 | OQ-INV-004, OQ-SYS-001, OQ-SYS-004 | LEG-INV-001, LEG-INV-002, LEG-INV-003 | Inventory |
| FR-MFG-001 | BR-MFG-001, BR-MFG-004, BR-SYS-001 | OQ-MFG-004, OQ-SYS-001 | LEG-MFG-003, LEG-MFG-005 | Manufacturing |
| FR-MFG-002 | BR-MFG-002, BR-INV-003, BR-SYS-001 | OQ-MFG-001, OQ-SYS-001, OQ-SYS-004 | LEG-MFG-001, LEG-MFG-003, LEG-MFG-004, LEG-INV-001, LEG-INV-002 | Manufacturing / Inventory |
| FR-MFG-003 | BR-MFG-003 | OQ-MFG-003 | LEG-MFG-003, LEG-MFG-006 | Manufacturing |
| FR-MFG-004 | BR-MFG-003, BR-MFG-004, BR-INV-003, BR-SYS-001 | OQ-MFG-003, OQ-MFG-004, OQ-SYS-001, OQ-SYS-004 | LEG-MFG-003, LEG-MFG-005, LEG-MFG-006, LEG-INV-001, LEG-INV-002 | Manufacturing / Inventory |
| FR-SYS-001 | BR-SYS-001 | OQ-SYS-001 | LEG-MST-006 | System / Permission |
| FR-SYS-002 | BR-INV-003, BR-SYS-001 | OQ-SYS-001, OQ-SYS-004 | LEG-INV-002, LEG-MST-006 and V1 quantity-changing capabilities | System / Traceability |

## Legacy Coverage Summary

Coverage labels describe the relationship between the 30 Sprint 1 capabilities and this deliberately compact V1 requirement baseline:

- **COVERED IN V1:** directly represented by one or more functional requirements.
- **SUPPORTING / INDIRECT:** assumed master data or a view/reference capability used by requirements without its own detailed workflow.
- **DEFERRED:** intentionally left for a later release or analysis phase.
- **NEEDS CLARIFICATION:** no target direction can be selected until the remaining business question is resolved.

| Legacy ID | Legacy Capability | V1 Coverage | Requirement / Reason |
|---|---|---|---|
| LEG-MST-001 | Product / Material Records | SUPPORTING / INDIRECT | Approved active items are preconditions across purchasing, sales, inventory, and manufacturing; detailed item maintenance is outside Sprint 2. |
| LEG-MST-002 | Supplier Records | SUPPORTING / INDIRECT | FR-PUR-001 assumes an active supplier; supplier-master workflow is outside Sprint 2. |
| LEG-MST-003 | Customer Records | SUPPORTING / INDIRECT | FR-SAL-001 assumes an active customer; customer-master workflow is outside Sprint 2. |
| LEG-MST-004 | Warehouse / Location Records | SUPPORTING / INDIRECT | Locations support receipts, deliveries, adjustments, transfers, and history; maintenance hierarchy is not specified. |
| LEG-MST-005 | Units of Measure | SUPPORTING / INDIRECT | Active units are assumed for transaction quantities; conversions and maintenance remain outside scope. |
| LEG-MST-006 | Users / Permissions | COVERED IN V1 | FR-SYS-001 and FR-SYS-002 define fixed role actions and responsible-user traceability. |
| LEG-PUR-001 | Purchase Request | COVERED IN V1 | FR-PUR-001 requires an approved request before a standard inventory Purchase Order. |
| LEG-PUR-002 | Purchase Order | COVERED IN V1 | FR-PUR-001, FR-PUR-002, and FR-PUR-004 cover origin, receipt states, and explicit closure. |
| LEG-PUR-003 | Goods Receipt | COVERED IN V1 | FR-PUR-002, FR-PUR-003, and FR-INV-001 cover valid posting, over-receipt blocking, and stock effect. |
| LEG-PUR-004 | Purchase Return | DEFERRED | Supplier-return references and stock timing were not selected for the V1 baseline. |
| LEG-PUR-005 | Supplier Quotation Comparison | DEFERRED | Sourcing and quotation comparison are outside the selected first-release flows. |
| LEG-PUR-006 | Purchase Status Inquiry | SUPPORTING / INDIRECT | FR-PUR-002 and FR-PUR-004 expose necessary state and remaining quantities; no separate inquiry workflow is specified. |
| LEG-SAL-001 | Sales Order | COVERED IN V1 | FR-SAL-001 through FR-SAL-004 cover confirmation, allocation, delivery constraints, and fulfillment state. |
| LEG-SAL-002 | Delivery | COVERED IN V1 | FR-SAL-002 and FR-SAL-003 define valid partial delivery and blocked excess delivery. |
| LEG-SAL-003 | Sales Return | DEFERRED | OQ-SAL-004 defers inspection, disposition, and return-to-available-stock behavior. |
| LEG-SAL-004 | Customer Price Reference | NEEDS CLARIFICATION | The source and governance of customer pricing remain undefined and complex pricing is out of scope. |
| LEG-SAL-005 | Sales Status Inquiry | SUPPORTING / INDIRECT | FR-SAL-004 provides required V1 fulfillment quantities and state without a separate inquiry specification. |
| LEG-INV-001 | Stock Position | COVERED IN V1 | Quantity effects are defined across FR-SAL-001, FR-INV-001 through FR-INV-005, and manufacturing posting requirements. |
| LEG-INV-002 | Stock Movement History | COVERED IN V1 | FR-SYS-002 defines mandatory history fields and atomic linkage to quantity changes. |
| LEG-INV-003 | Warehouse Transfer | COVERED IN V1 | FR-INV-004 and FR-INV-005 define dispatch, in-transit, and receipt behavior. |
| LEG-INV-004 | Stock Adjustment | COVERED IN V1 | FR-INV-002 and FR-INV-003 define authorized valid posting and negative-stock blocking. |
| LEG-INV-005 | Stock Opname | DEFERRED | Count, variance review, and posting stages were not selected for this compact baseline. |
| LEG-INV-006 | Inventory Reservation | COVERED IN V1 | FR-SAL-001 through FR-SAL-004 define V1 reservation and fulfillment behavior. |
| LEG-INV-007 | Lot / Batch Reference | NEEDS CLARIFICATION | Item classes requiring lot/batch traceability have not been defined. |
| LEG-MFG-001 | Bill of Materials | SUPPORTING / INDIRECT | FR-MFG-002 retains the applicable Bill of Materials quantity for comparison; versioning and approval remain outside scope. |
| LEG-MFG-002 | Production Planning | DEFERRED | Advanced planning and forecasting are outside the selected Production Order flow. |
| LEG-MFG-003 | Production Order / Work Order | COVERED IN V1 | FR-MFG-001 through FR-MFG-004 define state, consumption, and output controls. |
| LEG-MFG-004 | Material Consumption | COVERED IN V1 | FR-MFG-002 defines posting actual component consumption and recording variance. |
| LEG-MFG-005 | Production Execution Status | COVERED IN V1 | FR-MFG-001 and FR-MFG-004 define the limited V1 progress and completion states. |
| LEG-MFG-006 | Production Result | COVERED IN V1 | FR-MFG-003 and FR-MFG-004 define output limits, stock effect, and completion. |

## Coverage Boundary

The summary does not imply that all covered capabilities are fully specified for every future use case. It identifies only the V1 behaviors needed for the 19 approved fictional requirements. Deferred and clarification items create no hidden V1 requirements or test cases.
