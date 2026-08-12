# Legacy Feature Inventory

This inventory is an independently constructed, representative view of a generic manufacturing ERP. It intentionally avoids an exhaustive menu reconstruction. The 30 entries are **working-model capabilities**, not claims about a real legacy product. Their questions remain unresolved unless a confirmed case fact says otherwise.

| Legacy ID | Area | Legacy Capability | Business Purpose | Initial Migration Question |
|---|---|---|---|---|
| LEG-MST-001 | Master Data | Product / Material Records | Maintains identifying and descriptive information for purchased, produced, and sold items. | Should raw materials, intermediates, and finished goods use one item model with controlled types? |
| LEG-MST-002 | Master Data | Supplier Records | Maintains supplier identities and operational contact information. | Which supplier fields and lifecycle statuses are required in the web ERP? |
| LEG-MST-003 | Master Data | Customer Records | Maintains customer identities and delivery-related information. | Which customer attributes must be shared with sales and delivery processes? |
| LEG-MST-004 | Master Data | Warehouse / Location Records | Identifies storage facilities and internal stock locations. | Does the target need a warehouse hierarchy, simple locations, or both? |
| LEG-MST-005 | Master Data | Units of Measure | Provides quantity units used by operational transactions. | Are unit conversions required, and which roles may maintain them? |
| LEG-MST-006 | Master Data | Users / Permissions | Controls application access to functions and data. | How should legacy access choices translate into role-based permissions and approval authority? |
| LEG-PUR-001 | Purchasing | Purchase Request | Records an internal need for externally sourced items. | Is a request mandatory before every purchase order, and does it require approval? |
| LEG-PUR-002 | Purchasing | Purchase Order | Records a purchasing commitment to a supplier. | Which statuses, approval controls, and change restrictions should apply? |
| LEG-PUR-003 | Purchasing | Goods Receipt | Records delivery of ordered items into warehouse custody. | Can receipts be partial or exceed the ordered quantity? |
| LEG-PUR-004 | Purchasing | Purchase Return | Records goods sent back to a supplier. | Must every return reference a receipt, and when should stock decrease? |
| LEG-PUR-005 | Purchasing | Supplier Quotation Comparison | Supports comparison of supplier offers before selection. | Should quotation comparison remain separate or join a broader sourcing workspace? |
| LEG-PUR-006 | Purchasing | Purchase Status Inquiry | Provides visibility into request, order, and receipt progress. | Can fragmented status views become one traceable request-to-receipt view? |
| LEG-SAL-001 | Sales | Sales Order | Records a customer's requested items and quantities. | When is an order considered accepted, and should it reserve inventory? |
| LEG-SAL-002 | Sales | Delivery | Records goods released and shipped for a sales order. | Can delivery be partial, and what event decreases available or on-hand stock? |
| LEG-SAL-003 | Sales | Sales Return | Records customer goods returned after delivery. | What inspection or disposition is needed before returned stock becomes available? |
| LEG-SAL-004 | Sales | Customer Price Reference | Provides pricing information during order entry. | Is pricing a maintained reference, a calculated rule, or an external commercial decision? |
| LEG-SAL-005 | Sales | Sales Status Inquiry | Provides visibility into order and delivery progress. | Should order and fulfillment status be merged into a single sales workspace? |
| LEG-INV-001 | Inventory | Stock Position | Shows item quantities by warehouse or location. | Which quantity states—on hand, available, reserved, or in transit—must be visible? |
| LEG-INV-002 | Inventory | Stock Movement History | Records a chronological history of quantity-changing events. | What source-document and user details are required for traceability? |
| LEG-INV-003 | Inventory | Warehouse Transfer | Moves stock between warehouses or internal locations. | Is a transfer one-step or does it require issue, transit, and receipt states? |
| LEG-INV-004 | Inventory | Stock Adjustment | Corrects recorded quantity after an authorized reason. | Who may propose and approve corrections, and can they create negative stock? |
| LEG-INV-005 | Inventory | Stock Opname | Compares physical counts with system quantities. | Should count entry, variance review, and posting be separate controlled stages? |
| LEG-INV-006 | Inventory | Inventory Reservation | Marks quantity for an expected demand. | Which demand types may reserve stock, and when is a reservation released? |
| LEG-INV-007 | Inventory | Lot / Batch Reference | Associates inventory with a production or receipt grouping. | Is lot-level traceability required for all items or only selected item classes? |
| LEG-MFG-001 | Manufacturing | Bill of Materials | Defines component relationships for a manufactured item. | Does the target need versions, effective dates, or approval before use? |
| LEG-MFG-002 | Manufacturing | Production Planning | Organizes expected production demand and timing. | What planning horizon and level of detail belong in the first web release? |
| LEG-MFG-003 | Manufacturing | Production Order / Work Order | Authorizes production of a specified item and quantity. | Which statuses and approvals control release, change, cancellation, and closure? |
| LEG-MFG-004 | Manufacturing | Material Consumption | Records components used by production. | Are components deducted when issued, when reported as consumed, or automatically? |
| LEG-MFG-005 | Manufacturing | Production Execution Status | Records progress of active production work. | Which milestones provide useful visibility without recreating fragmented desktop steps? |
| LEG-MFG-006 | Manufacturing | Production Result | Records finished or intermediate output from production. | Can output exceed the planned quantity, and when does it become available stock? |
