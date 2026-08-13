from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTAL_CODE = (By.CSS_SELECTOR, '[data-test="postalCode"]')
    CONTINUE = (By.CSS_SELECTOR, '[data-test="continue"]')
    ERROR = (By.CSS_SELECTOR, '[data-test="error"]')
    ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    ITEM_NAME = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    ITEM_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    FINISH = (By.CSS_SELECTOR, '[data-test="finish"]')
    CONFIRMATION = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    def submit_customer_information(
        self, first_name: str = "", last_name: str = "", postal_code: str = ""
    ) -> None:
        if first_name:
            self.type_text(self.FIRST_NAME, first_name)
        if last_name:
            self.type_text(self.LAST_NAME, last_name)
        if postal_code:
            self.type_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)

    @property
    def error_message(self) -> str:
        return self.text(self.ERROR)

    def product_details(self, product_name: str) -> tuple[str, str]:
        item = self._item(product_name)
        return (
            item.find_element(*self.ITEM_NAME).text,
            item.find_element(*self.ITEM_PRICE).text,
        )

    def finish_order(self) -> None:
        self.click(self.FINISH)
        self.wait_for_url_contains("/checkout-complete.html")

    @property
    def confirmation_header(self) -> str:
        return self.text(self.CONFIRMATION)

    def _item(self, product_name: str) -> WebElement:
        for item in self.all_present(self.ITEMS):
            if item.find_element(*self.ITEM_NAME).text == product_name:
                return item
        raise NoSuchElementException(f"Checkout product not found: {product_name}")
