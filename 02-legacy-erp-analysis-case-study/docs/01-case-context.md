# Case Context

## Business Background

Northstar Components Manufacturing is a fictional mid-sized manufacturer producing industrial components. Its staff coordinate purchasing, customer orders, warehouse activity, and production using shared item, business-partner, and location information. The case uses synthetic organizational details and does not represent a real company or implementation.

## Legacy Situation

The working scenario begins with a desktop ERP that has accumulated functions over many years. Purchasing Staff, Sales Staff, Warehouse Staff, Production Staff, supervisors, and System Administrators use different parts of the application to support their work. Available inputs are an old application, incomplete documentation, fragmented knowledge of menus and functions, and stakeholder expectations for a future web ERP.

## Migration Problem

The analysis must make sense of fragmented menus, an aging desktop architecture, and unclear dependencies between transactions. Process visibility is limited, some business rules are undocumented, and the existing structure is difficult to integrate with a browser-based platform. A direct screen-for-screen conversion could reproduce legacy complexity without establishing whether each function still serves the intended business outcome.

These conditions are migration risks, not confirmed software defects. Sprint 1 does not infer failures, control gaps, or mandatory behavior that the fictional evidence has not established.

## Target

A browser-based ERP with integrated business flows and clearer navigation across the selected operational areas.

## In Scope

- Purchasing
- Sales
- Inventory
- Manufacturing
- Master Data and Permissions

## Out of Scope

- Detailed accounting implementation
- Payroll
- Customer relationship management
- Human resources information systems
- Tax filing
- Advanced forecasting
- Mobile applications
- Third-party integrations

Finance or accounting may be mentioned only when an operational event could have a downstream impact requiring later analysis.

## Analysis Objective

The objective is not simply to **copy desktop screens into web pages**. It is to understand the business intent behind representative legacy functions, reconstruct plausible high-level workflows, distinguish known case facts from working assumptions, and propose how capabilities should be retained, redesigned, merged, replaced, deprecated, or clarified for the target system.

Sprint 1 produces an analytical starting point. Migration decisions are analyst proposals, and unresolved behavior remains in the open-question register until the fictional case defines it in a later phase.

## Evidence Labels Used in This Sprint

- **Confirmed case fact:** explicitly established by this fictional portfolio brief, such as the selected modules or browser-based target.
- **Working model:** a clean-room representation used to organize analysis; it is not confirmed historical behavior.
- **Assumption:** a plausible interpretation that requires validation.
- **Analyst proposal:** a preliminary recommendation for the target system, not an approved requirement or historical decision.
