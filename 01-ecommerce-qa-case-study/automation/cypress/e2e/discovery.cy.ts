import testData from "../fixtures/test-data.json";

describe("Product discovery regression", () => {
  it("[TC-DISC-002 | SCN-DISC-002 | REQ-DISC-002] returns products for a known title keyword", () => {
    cy.startAnonymousSession();
    cy.get("#small-searchterms").type(testData.knownSearchKeyword);
    cy.get("button.search-box-button").click();

    cy.location("pathname").should("eq", "/search");
    cy.get(".product-title a")
      .should("have.length.greaterThan", 0)
      .then(($titles) => {
        const titles = [...$titles].map((element) => element.textContent?.trim() ?? "");
        expect(
          titles.some((title) =>
            title.toLowerCase().includes(testData.knownSearchKeyword.toLowerCase()),
          ),
        ).to.equal(true);
      });
  });

  it("[TC-DISC-003 | SCN-DISC-003 | REQ-DISC-003] displays the approved zero-result state", () => {
    cy.startAnonymousSession();
    const zeroResultQuery = `${testData.zeroResultPrefix}${Date.now()}`;
    cy.get("#small-searchterms").type(zeroResultQuery);
    cy.get("button.search-box-button").click();

    cy.get(".no-result")
      .should("be.visible")
      .and("contain.text", "No products were found that matched your criteria.");
    cy.get(".product-title a").should("not.exist");
  });

  it("[TC-DISC-005 | SCN-DISC-005 | REQ-DISC-005] restricts shoes to Nike products", () => {
    cy.startAnonymousSession();
    cy.visit(testData.manufacturerFilter.categoryPath);

    cy.get(".product-title a").should("have.length.greaterThan", 0).then(($before) => {
      const beforeCount = $before.length;
      cy.get(testData.manufacturerFilter.labelSelector).click();
      cy.get(testData.manufacturerFilter.checkboxSelector).should("be.checked");
      cy.location("search").should("contain", testData.manufacturerFilter.queryValue);
      cy.get(".product-title a")
        .should("have.length.greaterThan", 0)
        .and(($after) => {
          expect($after.length).to.be.lessThan(beforeCount);
          [...$after].forEach((element) => {
            expect(element.textContent?.trim()).to.contain(testData.manufacturerFilter.name);
          });
        });
    });
  });
});
