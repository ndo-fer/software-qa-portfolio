# REST API Test Design

## Target

Restful Booker — `https://restful-booker.herokuapp.com`

## Test Objective

Demonstrate compact, executable API QA coverage across HTTP status handling, authentication, positive and negative behavior, CRUD persistence, data integrity, dynamic variable chaining, and JSON contract validation.

## Environment Constraints

- The target is a public shared environment.
- Server data resets periodically and may change between requests.
- Booking IDs are dynamic.
- Every run must create its own disposable resource and clean up only that resource.
- Tests have no dependency on pre-existing booking IDs.
- Concurrent public activity and reset timing remain external sources of interference.

## Contract and Observation Basis

### DOCUMENTED API CONTRACT

The published Restful Booker behavior defines the health, authentication, booking list, create, detail, full update, partial update, and delete operations. The portfolio treats documented success statuses and documented response shapes as the primary contract.

### LIVE RECONNAISSANCE OBSERVATION

Approved reconnaissance observed `404` for an unknown booking ID, `403` for missing or invalid mutation authentication, `500` for a missing create payload, and `418` for an unsupported `Accept` value. During the Sprint 1 CLI run, the same unsupported `Accept` request returned `200`, showing that this header behavior is not stable. The `500` and prior `418` are recorded only as observed negative behavior; they are not defect claims or formalized API requirements.

### PORTFOLIO TEST EXPECTATION

The collection asserts the stable documented flow and the approved observed statuses. It creates and chains a runtime token and booking ID, verifies mutation persistence with follow-up reads, confirms protected state after rejected mutations, and deletes only the booking created by the current run.

## Endpoint Coverage

| Method | Endpoint | Coverage |
|---|---|---|
| GET | `/ping` | Health status |
| POST | `/auth` | Valid and invalid credentials; token capture |
| GET | `/booking` | Booking index availability and basic shape |
| POST | `/booking` | Valid creation, data echo, dynamic ID, create-envelope schema |
| GET | `/booking/:id` | Runtime detail, persistence, unknown ID, post-delete state |
| PUT | `/booking/:id` | Authenticated full replacement |
| PATCH | `/booking/:id` | Authenticated partial update and rejected unauthenticated mutation |
| DELETE | `/booking/:id` | Rejected invalid-token deletion and authenticated cleanup |

## Test Inventory

| Test ID | Method | Endpoint | Test Intent | Type | Priority |
|---|---|---|---|---|---|
| API-HEALTH-001 | GET | `/ping` | Return the documented health success status. | POSITIVE | P1 |
| API-AUTH-001 | POST | `/auth` | Generate and capture a non-empty token with valid credentials. | AUTHORIZATION | P1 |
| API-AUTH-002 | POST | `/auth` | Reject invalid credentials without issuing a valid token. | NEGATIVE | P1 |
| API-BOOK-001 | GET | `/booking` | Return an accessible booking index with array entries shaped as IDs. | CONTRACT | P2 |
| API-BOOK-002 | POST | `/booking` | Create a valid disposable booking and capture its dynamic ID. | STATEFUL CRUD | P1 |
| API-CONTRACT-001 | POST | `/booking` | Validate create-envelope schema and submitted data integrity. | CONTRACT | P1 |
| API-BOOK-003 | GET | `/booking/:id` | Retrieve the newly created booking and match submitted values. | DATA INTEGRITY | P1 |
| API-CONTRACT-002 | GET | `/booking/:id` | Validate the booking-detail JSON Schema. | CONTRACT | P1 |
| API-BOOK-004 | PUT | `/booking/:id` | Perform an authenticated full replacement across multiple fields. | STATEFUL CRUD | P1 |
| API-BOOK-005 | GET | `/booking/:id` | Verify the complete PUT representation persisted. | DATA INTEGRITY | P1 |
| API-BOOK-006 | PATCH | `/booking/:id` | Mutate selected fields with authentication. | STATEFUL CRUD | P1 |
| API-BOOK-007 | GET | `/booking/:id` | Verify PATCH changes and unchanged fields persisted. | DATA INTEGRITY | P1 |
| API-NEG-001 | PATCH | `/booking/:id` | Reject a mutation without authentication and preserve state. | AUTHORIZATION | P1 |
| API-NEG-002 | DELETE | `/booking/:id` | Reject deletion with an invalid token and preserve the resource. | AUTHORIZATION | P1 |
| API-NEG-003 | GET / POST | `/booking/:id`, `/booking` | Record observed unknown-ID `404` and missing-payload `500` behavior. | NEGATIVE | P2 |
| API-NEG-004 | GET | `/booking` | Observe unsupported-`Accept` handling; known live outcomes are ignored (`200`) or rejected (`418`). | HEADER / CONTENT NEGOTIATION | P2 |

## Stateful Execution Flow

`AUTH → CREATE disposable booking → capture bookingId → GET → PUT → GET/verify → PATCH → GET/verify → authorization negatives → observed negatives → DELETE own booking → GET after delete`

Collection runs continue after ordinary assertion failures, so the ordered `99 Cleanup` folder still gets a reasonable opportunity to delete `{{bookingId}}`. Cleanup never enumerates or deletes other public bookings.
