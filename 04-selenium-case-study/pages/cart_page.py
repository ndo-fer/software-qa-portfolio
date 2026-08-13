from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class CartPage(BasePage):
    ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    ITEM_NAME = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    ITEM_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    CHECKOUT = (By.CSS_SELECTOR, '[data-test="checkout"]')

    def product_details(self, product_name: str) -> tuple[str, str]:
        item = self._item(product_name)
        return (
            item.find_element(*self.ITEM_NAME).text,
            item.find_element(*self.ITEM_PRICE).text,
        )

    def contains_product(self, product_name: str) -> bool:
        return any(
            item.find_element(*self.ITEM_NAME).text == product_name
            for item in self.driver.find_elements(*self.ITEMS)
        )

    def remove_product(self, product_name: str) -> None:
        self._item(product_name)
        slug = product_name.lower().replace(" ", "-")
        self.click((By.CSS_SELECTOR, f'[data-test="remove-{slug}"]'))
        self.wait.until(lambda _driver: not self.contains_product(product_name))

    def begin_checkout(self) -> None:
        self.click(self.CHECKOUT)
        self.wait_for_url_contains("/checkout-step-one.html")

    def _item(self, product_name: str) -> WebElement:
        for item in self.all_present(self.ITEMS):
            if item.find_element(*self.ITEM_NAME).text == product_name:
                return item
        raise NoSuchElementException(f"Cart product not found: {product_name}")
