# Restful Booker API Testing Case Study

[![Postman API CI](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/postman-api.yml/badge.svg?branch=main)](https://github.com/ndo-fer/software-qa-portfolio/actions/workflows/postman-api.yml)

**Status:** COMPLETE — REST API Testing and CI

This case study uses [Restful Booker](https://restful-booker.herokuapp.com/) to cover health checks, authentication, CRUD, negative authorization, response contracts, and cleanup in a shared public environment. Because the service resets periodically, each run creates and deletes its own booking.

## Coverage

The collection covers `GET /ping`, `POST /auth`, `GET /booking`, `POST /booking`, `GET /booking/:id`, `PUT /booking/:id`, `PATCH /booking/:id`, and `DELETE /booking/:id`.

The suite contains **16 designed API test cases**, implemented as **19 ordered collection requests** with **47 assertions** and **2 JSON Schema checks**. Test categories include positive, negative, authorization, contract, stateful CRUD, header/content negotiation, and data integrity.

Authenticated full replacement (`PUT`) changes the complete booking representation and is verified by a follow-up read. Authenticated partial mutation (`PATCH`) changes only selected fields; tests verify both changed values and untouched state. Missing and invalid authentication are rejected, followed by reads that prove the runtime resource remains protected.

## Isolation and authentication

Each run generates unique `runtimeFirstName` and `runtimeLastName` values, creates one disposable booking, captures its `bookingId`, and mutates only that resource. The run captures an authentication `token` from `POST /auth`; authenticated mutations send it as a token cookie. Negative authorization requests deliberately omit or invalidate that cookie. Cleanup deletes only `{{bookingId}}` and verifies that the resource is no longer available.

The environment file contains the public base URL but no populated password. Supply Restful Booker's published testing credentials at runtime:

```powershell
postman collection run postman/restful-booker.postman_collection.json `
  --environment postman/restful-booker.postman_environment.json `
  --env-var "username=<published-test-username>" `
  --env-var "password=<published-test-password>" `
  --reporters "cli,junit" `
  --reporter-junit-export reports/postman-cli-junit.xml
```

This is local-file execution and requires no Postman Cloud API key.

## Collection structure

1. `00 Health` — service health check
2. `01 Authentication` — valid and invalid credential behavior
3. `02 Booking Lifecycle` — list, create, read, PUT, PATCH, and persistence checks
4. `03 Negative Authorization` — rejected mutations and protected-state verification
5. `04 Negative / Contract` — unknown ID, missing payload, and content-negotiation observations
6. `99 Cleanup` — authenticated deletion and post-delete verification

## Execution results

| Execution | Result | Requests | Assertions | Failed | Evidence |
|---|---:|---:|---:|---:|---|
| Local Postman CLI 1.45.0 | PASS | 19 | 47 | 0 | Committed JUnit report |
| GitHub Actions, Ubuntu 24.04 | PASS | 19 | 47 | 0 | [Hosted run](https://github.com/ndo-fer/software-qa-portfolio/actions/runs/31580305791) and uploaded `postman-api-junit` artifact |

The workflow uses `actions/checkout@v4`, the official `postmanlabs/postman-cli-action@v1`, and Postman CLI 1.45.0—the same version verified locally. It runs the committed collection and environment files without a Postman Cloud collection ID or API key. Repository secrets are injected as runtime environment variables, and the generated CI JUnit report is uploaded with `actions/upload-artifact@v4` even when a test step fails.

## Shared-environment limitation

Restful Booker is public and periodically resets, so service availability, reset timing, and concurrent users remain external constraints. The collection minimizes interference by generating a unique identity, creating one disposable booking, chaining its dynamic `bookingId`, and deleting only that resource.

Unsupported `Accept` handling is deliberately treated as non-contractual observation rather than a defect: reconnaissance observed `418`, while completed local and hosted runs returned `200`. The assertion records either known observed outcome without changing the strict CRUD, authentication, schema, or persistence expectations.

## Artifacts

- [API test design](docs/01-api-test-design.md)
- [Postman collection](postman/restful-booker.postman_collection.json)
- [Postman environment](postman/restful-booker.postman_environment.json)
- [Local JUnit report](reports/postman-cli-junit.xml)
- [GitHub Actions workflow](../.github/workflows/postman-api.yml)
