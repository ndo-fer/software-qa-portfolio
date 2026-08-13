from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import PASSWORD, STANDARD_USER


def test_added_product_information_is_preserved_in_cart(driver):
    product = "Sauce Labs Backpack"
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.load()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_until_loaded()
    inventory_name, inventory_price = inventory_page.product_details(product)
    inventory_page.add_product(product)

    assert inventory_page.cart_badge == "1"

    inventory_page.open_cart()
    cart_name, cart_price = cart_page.product_details(product)

    assert cart_page.contains_product(product)
    assert cart_name == inventory_name
    assert cart_price == inventory_price


def test_add_two_products_then_remove_one(driver):
    removed_product = "Sauce Labs Backpack"
    remaining_product = "Sauce Labs Bike Light"
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.load()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_until_loaded()
    inventory_page.add_product(removed_product)
    inventory_page.add_product(remaining_product)

    assert inventory_page.cart_badge == "2"

    inventory_page.open_cart()
    cart_page.remove_product(removed_product)

    assert inventory_page.cart_badge == "1"
    assert not cart_page.contains_product(removed_product)
    assert cart_page.contains_product(remaining_product)
