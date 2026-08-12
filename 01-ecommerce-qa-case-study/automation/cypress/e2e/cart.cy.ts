import testData from "../fixtures/test-data.json";

const parseMoney = (value: string): number =>
  Number(value.replace(/[^0-9.-]+/g, ""));

describe("Cart regression", () => {
  it("[TC-CART-001 | SCN-CART-001 | REQ-CART-001] recalculates subtotal and total for quantity two", () => {
    cy.startAnonymousSession();
    cy.addSimpleProductToCart(testData.simpleProduct.path, testData.simpleProduct.addButton);
    cy.visit("/cart");

    cy.get(".product-unit-price").invoke("text").then((unitPriceText) => {
      const unitPrice = parseMoney(unitPriceText);
      cy.get(".product-subtotal").invoke("text").then((initialSubtotalText) => {
        const initialSubtotal = parseMoney(initialSubtotalText);
        cy.get("input.qty-input").clear().type("2").blur();

        cy.get("input.qty-input").should("have.value", "2");
        const expectedTotal = unitPrice * 2;
        cy.get(".product-subtotal").should(($subtotal) => {
          expect(parseMoney($subtotal.text())).to.equal(expectedTotal);
          expect(parseMoney($subtotal.text())).to.equal(initialSubtotal * 2);
        });
        cy.get(".order-total .value-summary").should(($total) => {
          expect(parseMoney($total.text())).to.equal(expectedTotal);
        });
      });
    });
  });

  it("[TC-CART-005 | SCN-CART-009 | REQ-CART-005] merges identical configured products into one row", () => {
    cy.startAnonymousSession();
    cy.addConfiguredProductToCart(
      testData.configurableProduct.path,
      testData.configurableProduct.addButton,
      testData.configurableProduct.configurationA,
    );
    cy.addConfiguredProductToCart(
      testData.configurableProduct.path,
      testData.configurableProduct.addButton,
      testData.configurableProduct.configurationA,
    );
    cy.visit("/cart");

    cy.get("table.cart tbody tr").should("have.length", 1);
    cy.get("input.qty-input").should("have.value", "2");
    cy.get("table.cart tbody tr .attributes")
      .should("contain.text", testData.configurableProduct.configurationA.processor)
      .and("contain.text", testData.configurableProduct.configurationA.ram)
      .and("contain.text", testData.configurableProduct.configurationA.hddSummary)
      .and("contain.text", testData.configurableProduct.configurationA.osSummary)
      .and("contain.text", testData.configurableProduct.configurationA.softwareSummary);
  });

  it("[TC-CART-006 | SCN-CART-010 | REQ-CART-006] creates separate rows for different configurations", () => {
    cy.startAnonymousSession();
    cy.addConfiguredProductToCart(
      testData.configurableProduct.path,
      testData.configurableProduct.addButton,
      testData.configurableProduct.configurationA,
    );
    cy.addConfiguredProductToCart(
      testData.configurableProduct.path,
      testData.configurableProduct.addButton,
      testData.configurableProduct.configurationB,
    );
    cy.visit("/cart");

    cy.get("table.cart tbody tr").should("have.length", 2);
    cy.get("table.cart tbody tr .attributes").then(($summaries) => {
      const summaries = [...$summaries].map((element) => element.textContent ?? "");
      expect(summaries.some((text) => text.includes(testData.configurableProduct.configurationA.ram))).to.equal(true);
      expect(summaries.some((text) => text.includes(testData.configurableProduct.configurationB.ram))).to.equal(true);
      expect(new Set(summaries).size).to.equal(2);
    });
  });
});
