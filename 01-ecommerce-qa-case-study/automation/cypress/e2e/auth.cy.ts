import testData from "../fixtures/test-data.json";

describe("Authentication regression", () => {
  it("[TC-AUTH-003 | SCN-AUTH-004, SCN-AUTH-005, SCN-AUTH-006 | REQ-AUTH-004] rejects invalid login and clears credentials", () => {
    cy.startAnonymousSession();
    cy.visit("/login");

    const uniqueEmail = `${testData.zeroResultPrefix}${Date.now()}@example.invalid`;
    cy.get("#Email").type(uniqueEmail);
    cy.get("#Password").type(`invalid-${Date.now()}`, { log: false });
    cy.get("button.login-button").click();

    cy.get(".message-error")
      .should("be.visible")
      .and("contain.text", "Login was unsuccessful");
    cy.get("#Email").should("have.value", "");
    cy.get("#Password").should("have.value", "");
    cy.get("a.ico-login").should("be.visible");
    cy.get("a.ico-account").should("not.exist");
  });

  it("[TC-AUTH-004 | SCN-AUTH-007 | REQ-AUTH-005] redirects anonymous protected-page access to login", () => {
    cy.startAnonymousSession();
    cy.visit(testData.protectedCustomerPath);

    cy.location("pathname").should("eq", "/login");
    cy.get(".page-title").should("contain.text", "Welcome, Please Sign In!");
    cy.get("a.ico-login").should("be.visible");
  });
});
