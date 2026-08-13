from decimal import Decimal

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    CONTAINER = (By.CSS_SELECTOR, '[data-test="inventory-container"]')
    ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    ITEM_NAME = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    ITEM_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    SORT = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    CART_LINK = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.CSS_SELECTOR, '[data-test="logout-sidebar-link"]')

    def wait_until_loaded(self) -> None:
        self.wait_for_url_contains("/inventory.html")
        self.visible(self.CONTAINER)

    @property
    def inventory_visible(self) -> bool:
        return self.is_visible(self.CONTAINER)

    def product_details(self, product_name: str) -> tuple[str, str]:
        item = self._item(product_name)
        return (
            item.find_element(*self.ITEM_NAME).text,
            item.find_element(*self.ITEM_PRICE).text,
        )

    def displayed_prices(self) -> list[Decimal]:
        return [self._price(element.text) for element in self.all_present(self.ITEM_PRICE)]

    def sort_by_price_low_to_high(self) -> None:
        Select(self.visible(self.SORT)).select_by_value("lohi")
        self.wait.until(lambda _driver: self.displayed_prices() == sorted(self.displayed_prices()))

    def add_product(self, product_name: str) -> None:
        self._item(product_name)
        self.click(self._product_control("add-to-cart", product_name))

    def remove_product(self, product_name: str) -> None:
        self.click(self._product_control("remove", product_name))

    @property
    def cart_badge(self) -> str | None:
        elements = self.driver.find_elements(*self.CART_BADGE)
        return elements[0].text if elements else None

    def open_cart(self) -> None:
        self.click(self.CART_LINK)
        self.wait_for_url_contains("/cart.html")

    def logout(self) -> None:
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)

    def _item(self, product_name: str) -> WebElement:
        for item in self.all_present(self.ITEMS):
            if item.find_element(*self.ITEM_NAME).text == product_name:
                return item
        raise NoSuchElementException(f"Inventory product not found: {product_name}")

    @staticmethod
    def _price(value: str) -> Decimal:
        return Decimal(value.removeprefix("$"))

    @staticmethod
    def _product_control(action: str, product_name: str) -> tuple[str, str]:
        slug = product_name.lower().replace(" ", "-")
        return By.CSS_SELECTOR, f'[data-test="{action}-{slug}"]'
