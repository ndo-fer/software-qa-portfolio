from decimal import Decimal

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
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
    MENU_WRAP = (By.CSS_SELECTOR, ".bm-menu-wrap")
    LOGOUT_LINK = (By.CSS_SELECTOR, '[data-test="logout-sidebar-link"]')
    LOGIN_USERNAME = (By.CSS_SELECTOR, '[data-test="username"]')

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
        add_control = self._product_control("add-to-cart", product_name)
        remove_control = self._product_control("remove", product_name)
        self.click(add_control)
        self.clickable(remove_control)
        self.wait.until(EC.invisibility_of_element_located(add_control))

    def remove_product(self, product_name: str) -> None:
        remove_control = self._product_control("remove", product_name)
        add_control = self._product_control("add-to-cart", product_name)
        self.click(remove_control)
        self.clickable(add_control)
        self.wait.until(EC.invisibility_of_element_located(remove_control))

    @property
    def cart_badge(self) -> str | None:
        elements = self.driver.find_elements(*self.CART_BADGE)
        return elements[0].text if elements else None

    def open_cart(self) -> None:
        self.click(self.CART_LINK)
        self.wait_for_url_contains("/cart.html")

    def logout(self) -> None:
        self.click(self.MENU_BUTTON)
        self._wait_for_menu_open_and_settled()
        logout_link = self.clickable(self.LOGOUT_LINK)
        logout_link.send_keys(Keys.ENTER)
        self.wait.until(EC.url_to_be("https://www.saucedemo.com/"))
        self.visible(self.LOGIN_USERNAME)

    def _wait_for_menu_open_and_settled(self) -> None:
        identity_transforms = {
            "none",
            "matrix(1, 0, 0, 1, 0, 0)",
            "matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)",
        }

        def menu_is_settled(_driver):
            menu_wrap = self.visible(self.MENU_WRAP)
            return (
                menu_wrap.get_attribute("aria-hidden") == "false"
                and menu_wrap.value_of_css_property("transform") in identity_transforms
            )

        self.wait.until(menu_is_settled)

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
