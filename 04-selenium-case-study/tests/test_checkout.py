from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import PASSWORD, STANDARD_USER


def test_required_customer_information_validation(driver):
    product = "Sauce Labs Backpack"
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.load()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_until_loaded()
    inventory_page.add_product(product)
    inventory_page.open_cart()
    cart_page.begin_checkout()

    checkout_page.submit_customer_information()

    assert checkout_page.error_message == "Error: First Name is required"
    assert "/checkout-step-one.html" in driver.current_url


def test_complete_checkout_successfully(driver):
    product = "Sauce Labs Backpack"
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.load()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_until_loaded()
    inventory_page.add_product(product)
    inventory_page.open_cart()
    cart_page.begin_checkout()
    checkout_page.submit_customer_information("QA", "Portfolio", "12345")
    checkout_page.wait_for_url_contains("/checkout-step-two.html")
    checkout_page.finish_order()

    assert checkout_page.confirmation_header == "Thank you for your order!"
    assert "/checkout-complete.html" in driver.current_url
    assert inventory_page.cart_badge is None


def test_selected_item_is_consistent_through_checkout_overview(driver):
    product = "Sauce Labs Backpack"
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.load()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_until_loaded()
    inventory_name, inventory_price = inventory_page.product_details(product)
    inventory_page.add_product(product)
    inventory_page.open_cart()
    cart_name, cart_price = cart_page.product_details(product)

    assert cart_name == inventory_name
    assert cart_price == inventory_price

    cart_page.begin_checkout()
    checkout_page.submit_customer_information("QA", "Portfolio", "12345")
    checkout_page.wait_for_url_contains("/checkout-step-two.html")
    overview_name, overview_price = checkout_page.product_details(product)

    assert overview_name == inventory_name
    assert overview_price == inventory_price
