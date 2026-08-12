type ProductConfiguration = {
  processor: string;
  ram: string;
  hddSelector: string;
  hddSummary: string;
  osSelector: string;
  osSummary: string;
  softwareSelector: string;
  softwareSummary: string;
};

declare global {
  namespace Cypress {
    interface Chainable {
      startAnonymousSession(): Chainable<void>;
      addSimpleProductToCart(productPath: string, addButton: string): Chainable<void>;
      selectComputerConfiguration(configuration: ProductConfiguration): Chainable<void>;
      addConfiguredProductToCart(
        productPath: string,
        addButton: string,
        configuration: ProductConfiguration,
      ): Chainable<void>;
    }
  }
}

Cypress.Commands.add("startAnonymousSession", () => {
  cy.clearAllCookies();
  cy.clearAllLocalStorage();
  cy.visit("/");
  cy.get("a.ico-login").should("be.visible");
  cy.get(".cart-qty").should("have.text", "(0)");
});

Cypress.Commands.add("addSimpleProductToCart", (productPath, addButton) => {
  cy.visit(productPath);
  cy.get(addButton).should("be.enabled").click();
  cy.get("#bar-notification .content")
    .should("be.visible")
    .and("contain.text", "The product has been added to your shopping cart");
  cy.get(".cart-qty").should("have.text", "(1)");
});

Cypress.Commands.add("selectComputerConfiguration", (configuration) => {
  cy.get("#product_attribute_1").select(configuration.processor);
  cy.get("#product_attribute_2").select(configuration.ram);
  cy.get(configuration.hddSelector).check();
  cy.get(configuration.osSelector).check();
  cy.get(configuration.softwareSelector).check();
});

Cypress.Commands.add(
  "addConfiguredProductToCart",
  (productPath, addButton, configuration) => {
    cy.visit(productPath);
    cy.selectComputerConfiguration(configuration);
    cy.get(addButton).should("be.enabled").click();
    cy.get("#bar-notification .content")
      .should("be.visible")
      .and("contain.text", "The product has been added to your shopping cart");
  },
);

export {};
