# Open Question Register

These 20 questions are intentionally unanswered in Sprint 1. They identify decisions needed before analyst proposals can become approved requirements. Suggested decision owners are fictional stakeholder roles, not evidence that a particular governance structure already exists.

## Purchasing

| OQ ID | Module | Question | Why It Matters | Decision Needed From |
|---|---|---|---|---|
| OQ-PUR-001 | Purchasing | Is a purchase request mandatory before every purchase order, or are defined exceptions allowed? | Determines workflow entry points, traceability, and approval coverage. | Purchasing Manager |
| OQ-PUR-002 | Purchasing | Can a goods receipt record a partial delivery? | Determines outstanding-quantity tracking and purchase-order completion behavior. | Purchasing Manager and Warehouse Supervisor |
| OQ-PUR-003 | Purchasing | Can received quantity exceed the purchase-order quantity, and if so under what authority? | Determines tolerance validation and exception approval. | Purchasing Manager |
| OQ-PUR-004 | Purchasing | What status should a partially received purchase order have, and how may its remainder be closed? | Determines lifecycle visibility and prevents ambiguous open commitments. | Purchasing Manager |

## Sales

| OQ ID | Module | Question | Why It Matters | Decision Needed From |
|---|---|---|---|---|
| OQ-SAL-001 | Sales | At what point, if any, should a sales order reserve stock? | Defines available-quantity calculation and competition between orders. | Sales Manager and Warehouse Supervisor |
| OQ-SAL-002 | Sales | Can a sales order be fulfilled through partial deliveries? | Determines delivery creation, remaining quantities, and order completion. | Sales Manager |
| OQ-SAL-003 | Sales | What should happen when available stock is insufficient for an accepted order? | Determines whether the system blocks, backorders, escalates, or permits an exception. | Sales Manager and Operations Manager |
| OQ-SAL-004 | Sales | When may returned goods become available for sale again? | Determines whether inspection or disposition is required before inventory reuse. | Sales Manager and Warehouse Supervisor |

## Inventory

| OQ ID | Module | Question | Why It Matters | Decision Needed From |
|---|---|---|---|---|
| OQ-INV-001 | Inventory | At what stage of goods receipt should on-hand and available stock increase? | Defines transaction timing and cross-module quantity consistency. | Warehouse Supervisor and Operations Manager |
| OQ-INV-002 | Inventory | Can a stock adjustment create negative inventory? | Determines validation, exception handling, and inventory integrity controls. | Warehouse Supervisor and Operations Manager |
| OQ-INV-003 | Inventory | Who may propose, approve, and post stock corrections? | Establishes separation of duties and audit responsibility. | Operations Manager and System Administrator |
| OQ-INV-004 | Inventory | Does an inter-warehouse transfer require separate dispatch and receipt confirmations? | Determines in-transit visibility and source/destination stock timing. | Warehouse Supervisor |

## Manufacturing

| OQ ID | Module | Question | Why It Matters | Decision Needed From |
|---|---|---|---|---|
| OQ-MFG-001 | Manufacturing | When are components deducted from inventory: issue, reported consumption, or automatic backflush? | Defines material availability, variance handling, and inventory timing. | Production Manager and Warehouse Supervisor |
| OQ-MFG-002 | Manufacturing | May actual component consumption differ from the bill of materials, and who authorizes variance? | Determines validation and production-variance controls. | Production Manager |
| OQ-MFG-003 | Manufacturing | Can production output exceed the planned quantity? | Determines overproduction tolerance and approval behavior. | Production Manager |
| OQ-MFG-004 | Manufacturing | At what status does production output become available inventory? | Defines completion, receipt, and downstream fulfillment timing. | Production Manager and Warehouse Supervisor |

## Cross-Module / Permission

| OQ ID | Module | Question | Why It Matters | Decision Needed From |
|---|---|---|---|---|
| OQ-SYS-001 | Cross-module / Permission | Which roles may approve, cancel, reopen, or correct purchasing, sales, inventory, and production transactions? | Defines authorization boundaries and exceptional lifecycle controls. | Operations Manager and System Administrator |
| OQ-SYS-002 | Cross-module / Permission | Must approval authority vary by warehouse, transaction value, or item category? | Determines whether simple roles are sufficient or contextual rules are needed. | Operations Manager |
| OQ-SYS-003 | Cross-module / Permission | Which master-data changes require approval or effective dating? | Controls the impact of shared data changes on active transactions. | Operations Manager and System Administrator |
| OQ-SYS-004 | Cross-module / Permission | What source-document, timestamp, user, and reason details must appear in cross-module history? | Establishes the minimum audit and traceability model for the web ERP. | Operations Manager and System Administrator |
