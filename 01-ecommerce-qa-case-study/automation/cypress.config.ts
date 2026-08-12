import { defineConfig } from "cypress";

export default defineConfig({
  allowCypressEnv: false,
  e2e: {
    baseUrl: "https://demo.nopcommerce.com",
    specPattern: "cypress/e2e/**/*.cy.ts",
    supportFile: "cypress/support/e2e.ts",
    testIsolation: true,
  },
  screenshotOnRunFailure: true,
  video: false,
  retries: {
    runMode: 1,
    openMode: 0,
  },
});
