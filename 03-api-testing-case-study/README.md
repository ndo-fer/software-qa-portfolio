# Restful Booker API Testing Case Study

**Status:** Sprint 1 — API Collection and Local CLI Complete

This compact portfolio project uses Restful Booker because it exposes a practical HTTP surface for health checks, authentication, booking CRUD, negative authorization, and response-contract testing. Its public, resettable environment also makes test isolation an explicit part of the QA design.

## Coverage

The collection covers `GET /ping`, `POST /auth`, `GET /booking`, `POST /booking`, `GET /booking/:id`, `PUT /booking/:id`, `PATCH /booking/:id`, and `DELETE /booking/:id`.

Test categories include positive, negative, authorization, contract, stateful CRUD, header/content negotiation, and data-integrity checks. JSON Schema assertions validate the create envelope and booking detail contract.

## Isolation and authentication

Each run generates unique `runtimeFirstName` and `runtimeLastName` values, creates one disposable booking, captures its `bookingId`, and mutates only that resource. The run captures an authentication `token` from `POST /auth`; authenticated mutations send it as a token cookie. Negative authorization requests deliberately omit or invalidate that cookie. Cleanup deletes only `{{bookingId}}` and verifies that the resource is no longer available.

The environment file contains the public base URL but no populated password. Supply Restful Booker's published testing credentials at runtime:

```powershell
postman collection run postman/restful-booker.postman_collection.json `
  --environment postman/restful-booker.postman_environment.json `
  --env-var "username=<published-test-username>" `
  --env-var "password=<published-test-password>" `
  --reporters cli,junit `
  --reporter-junit-export reports/postman-cli-junit.xml
```

This is local-file execution and requires no Postman Cloud API key.

## Collection structure

1. `00 Health` — service health check
2. `01 Authentication` — valid and invalid credential behavior
3. `02 Booking Lifecycle` — list, create, read, PUT, PATCH, and persistence checks
4. `03 Negative Authorization` — rejected mutations and protected-state verification
5. `04 Negative / Contract` — unknown ID and observed 500/418 behavior
6. `99 Cleanup` — authenticated deletion and post-delete verification

## Local execution result

The local Postman CLI run completed successfully: **19 requests, 47 assertions passed, 0 failed**, in **7.5 seconds**. A concise JUnit report is committed for reproducibility. Because the target is public and periodically resets, a future run can be affected by service availability, reset timing, or concurrent users; the collection minimizes that risk by never depending on a pre-existing booking ID.

- [API test design](docs/01-api-test-design.md)
- [Postman collection](postman/restful-booker.postman_collection.json)
- [JUnit run report](reports/postman-cli-junit.xml)

Continuous integration is intentionally out of scope until Sprint 2.
