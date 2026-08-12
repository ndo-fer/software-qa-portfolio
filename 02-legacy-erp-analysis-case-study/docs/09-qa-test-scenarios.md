# QA Test Scenarios

## Purpose and Basis

These risk-based scenarios derive exclusively from the 19 approved fictional V1 functional requirements and 13 business rules in the [Mini SRD](07-mini-srd.md). They describe test intent for a future implementation; they do not assert observed product behavior or execution results. Scenario depth follows inventory, authorization, state, and cross-module risk rather than equal coverage per requirement.

## Scenario Inventory

| Scenario ID | Requirement ID | Module | Scenario | Test Technique | Priority |
|---|---|---|---|---|---|
| SCN-PUR-001 | FR-PUR-001 | Purchasing | Create an `OPEN` Purchase Order from approved PR-001, retain the request reference and ordered quantity, and leave inventory unchanged. | DECISION / BUSINESS RULE | P2 |
| SCN-PUR-002 | FR-PUR-002 | Purchasing | Post a partial Goods Receipt against an `OPEN` Purchase Order and verify the remaining quantity, `PARTIALLY RECEIVED` state, destination on-hand increase, and history record. | CROSS-MODULE | P1 |
| SCN-PUR-003 | FR-PUR-002 | Purchasing | Post a Goods Receipt exactly equal to the Purchase Order line's remaining quantity and verify the order becomes `RECEIVED`. | BOUNDARY VALUE | P1 |
| SCN-PUR-004 | FR-PUR-003 | Purchasing | With remaining quantity 10, attempt to post receipt quantity 11 and verify rejection leaves receipt, order, inventory, and history unchanged. | BOUNDARY VALUE | P1 |
| SCN-PUR-005 | FR-PUR-004 | Purchasing | As an authorized Manager / Approver, close an outstanding remainder from `OPEN` or `PARTIALLY RECEIVED` and verify the order becomes `CLOSED` and accepts no further receipt. | STATE TRANSITION | P2 |
| SCN-PUR-006 | FR-PUR-002, FR-INV-001, FR-SYS-002 | Purchasing | Verify a posted Goods Receipt changes destination on-hand and Purchase Order remaining quantity exactly once and creates one linked inventory-history record. | DATA INTEGRITY | P1 |
| SCN-SAL-001 | FR-SAL-001 | Sales | Confirm a Sales Order when available quantity is sufficient and verify full reservation, zero unallocated quantity, and unchanged on-hand quantity. | POSITIVE | P1 |
| SCN-SAL-002 | FR-SAL-001 | Sales | Confirm an order for 100 when available quantity is 60 and verify reservation 60, unallocated quantity 40, and unchanged on-hand quantity. | BOUNDARY VALUE | P1 |
| SCN-SAL-003 | FR-SAL-002 | Sales | Post a partial Delivery within reserved and outstanding quantities and verify decreases to on-hand, reservation, and outstanding quantity plus `PARTIALLY DELIVERED` state and history. | CROSS-MODULE | P1 |
| SCN-SAL-004 | FR-SAL-002 | Sales | Post a Delivery exactly equal to the outstanding quantity and verify the Sales Order becomes `DELIVERED`. | STATE TRANSITION | P1 |
| SCN-SAL-005 | FR-SAL-003 | Sales | Attempt a Delivery above reserved or outstanding quantity and verify rejection identifies the limiting quantity and preserves order, reservation, inventory, and history. | NEGATIVE | P1 |
| SCN-SAL-006 | FR-SAL-004 | Sales | Verify requested, reserved, unallocated, delivered, and outstanding quantities agree with the displayed `CONFIRMED`, `PARTIALLY DELIVERED`, or `DELIVERED` state. | DATA INTEGRITY | P2 |
| SCN-INV-001 | FR-INV-002 | Inventory | Post an approved positive stock adjustment with creator, reason, approver, posting user, and timestamp and verify one stock and history increase. | DATA INTEGRITY | P1 |
| SCN-INV-002 | FR-INV-002 | Inventory | Post a negative adjustment that makes resulting on-hand quantity exactly zero and verify it is accepted with the required metadata and history. | BOUNDARY VALUE | P1 |
| SCN-INV-003 | FR-INV-003 | Inventory | With on-hand quantity 10, attempt adjustment -11 and verify negative-stock rejection leaves adjustment, stock, and history unchanged. | BOUNDARY VALUE | P1 |
| SCN-INV-004 | FR-INV-004 | Inventory | Dispatch a valid transfer and verify `DISPATCHED / IN TRANSIT`, source stock decrease, unchanged destination stock, in-transit quantity, and source history. | CROSS-MODULE | P1 |
| SCN-INV-005 | FR-INV-005 | Inventory | Receive a dispatched transfer and verify `RECEIVED`, one destination stock increase, no further source decrease, removal from in-transit quantity, and destination history. | CROSS-MODULE | P1 |
| SCN-INV-006 | FR-INV-004, FR-INV-005 | Inventory | Verify the approved transfer progression `DRAFT` → `DISPATCHED / IN TRANSIT` → `RECEIVED` with quantity effects only at dispatch and receipt. | STATE TRANSITION | P2 |
| SCN-INV-007 | FR-INV-001 | Inventory | Attempt to post the same Goods Receipt again and verify destination on-hand quantity and inventory history retain only the first posting effect. | DATA INTEGRITY | P1 |
| SCN-INV-008 | FR-SYS-002 | Inventory | For a posted quantity-changing transaction, verify the linked history contains every mandatory field and the quantity change is not persisted without that history. | DATA INTEGRITY | P1 |
| SCN-MFG-001 | FR-MFG-001 | Manufacturing | Move an authorized Production Order from `PLANNED` to `RELEASED` and retain the accepted state and responsible user. | STATE TRANSITION | P2 |
| SCN-MFG-002 | FR-MFG-001 | Manufacturing | Move an authorized Production Order from `RELEASED` to `IN PROGRESS` and retain the accepted state and responsible user. | STATE TRANSITION | P2 |
| SCN-MFG-003 | FR-MFG-001 | Manufacturing | Attempt to skip from `PLANNED` to `IN PROGRESS` and verify rejection leaves the Production Order state unchanged. | NEGATIVE | P1 |
| SCN-MFG-004 | FR-MFG-002 | Manufacturing | Post actual consumption 12 against Bill of Materials quantity 10 and verify component stock decreases by 12, variance +2 is retained, and linked history is created without a tolerance-tier assertion. | CROSS-MODULE | P1 |
| SCN-MFG-005 | FR-MFG-004 | Manufacturing | Post partial output 40 for planned quantity 100 and verify finished stock increases by 40, cumulative output is 40, and the order remains `IN PROGRESS`. | CROSS-MODULE | P1 |
| SCN-MFG-006 | FR-MFG-004 | Manufacturing | With cumulative output 40 and remaining planned quantity 60, post output 60 and verify the stock increase, cumulative output 100, and `COMPLETED` state. | BOUNDARY VALUE | P1 |
| SCN-MFG-007 | FR-MFG-003 | Manufacturing | With remaining planned quantity 10, attempt output 11 and verify rejection preserves the unposted result, Production Order state, output totals, inventory, and history. | BOUNDARY VALUE | P1 |
| SCN-SYS-001 | FR-SYS-001 | System / Permission | Verify a user whose role grants the requested module action may proceed to the applicable business-rule validation without the action being rejected for authorization. | AUTHORIZATION | P1 |
| SCN-SYS-002 | FR-SYS-001 | System / Permission | Attempt a controlled action without its role grant and verify authorization rejection leaves transaction state, inventory, and history unchanged. | AUTHORIZATION | P1 |
| SCN-SYS-003 | FR-SYS-002 | System / Traceability | Verify a successful quantity update and its complete linked history record persist together, including document ID, type, time, user, signed quantity, item, and relevant locations. | DATA INTEGRITY | P1 |

## Traceability Note

Scenario IDs link forward to the selected detailed cases in `10-selected-erp-test-cases.xlsx`. Requirement and business-rule IDs link backward through the Sprint 2 traceability matrix to synthetic stakeholder decisions, Sprint 1 open questions, and reconstructed legacy capabilities. The workbook Coverage sheet records whether each scenario is detailed, covered by a combined case, or retained at scenario level only.

## Test Design Summary

- **Total scenarios:** 30
- **Priority:** P1 24; P2 6; P3 0
- **By module:** Purchasing 6; Sales 6; Inventory 8; Manufacturing 7; System 3
- **Techniques used:** POSITIVE 1; NEGATIVE 2; BOUNDARY VALUE 7; STATE TRANSITION 5; DECISION / BUSINESS RULE 1; AUTHORIZATION 2; DATA INTEGRITY 6; CROSS-MODULE 6
- **Requirements covered:** 19 of 19
- **Selected for detailed design:** 16 test cases representing all 17 MUST requirements
- **Scenario-only:** 8 scenarios — SCN-PUR-003, SCN-PUR-005, SCN-SAL-004, SCN-SAL-006, SCN-INV-002, SCN-INV-006, SCN-MFG-003, and SCN-SYS-001. These retain alternative boundaries, status visibility, or focused state/authorization coverage without duplicating the selected cases.

## Execution Boundary

Northstar Components Manufacturing is a fictional clean-room case and has no implemented system under test. These artifacts demonstrate test analysis and design. No execution result is claimed.
