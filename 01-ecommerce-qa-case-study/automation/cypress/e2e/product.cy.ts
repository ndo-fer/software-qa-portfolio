import testData from "../fixtures/test-data.json";

describe("Product detail regression", () => {
  it("[TC-PDP-001 | SCN-PDP-001, SCN-PDP-002 | REQ-PDP-001] displays simple-product purchase information", () => {
    cy.startAnonymousSession();
    cy.visit(testData.simpleProduct.path);

    cy.get(".product-name h1").should("have.text", testData.simpleProduct.title);
    cy.get(".sku .value").should("have.text", testData.simpleProduct.sku);
    cy.get(".product-price").should("contain.text", testData.simpleProduct.price);
    cy.get("input.qty-input").should("be.visible").and("have.value", "1");
    cy.get(testData.simpleProduct.addButton).should("be.visible").and("be.enabled");
    cy.get(".attributes").should("not.exist");
  });

  it("[TC-PDP-002 | SCN-PDP-003 | REQ-PDP-002] blocks an incomplete required configuration", () => {
    cy.startAnonymousSession();
    cy.visit(testData.configurableProduct.path);
    cy.get(".cart-qty").should("have.text", "(0)");

    cy.get(testData.configurableProduct.addButton).click();

    cy.get("#bar-notification .content")
      .should("be.visible")
      .and("contain.text", "Please select RAM")
      .and("contain.text", "Please select HDD");
    cy.get(".cart-qty").should("have.text", "(0)");
  });
});
