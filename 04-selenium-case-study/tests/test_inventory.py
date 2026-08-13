from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import PASSWORD, STANDARD_USER


def test_sort_products_by_price_low_to_high(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_until_loaded()
    prices_before = inventory_page.displayed_prices()

    inventory_page.sort_by_price_low_to_high()
    prices_after = inventory_page.displayed_prices()

    assert len(prices_before) == len(prices_after)
    assert prices_after == sorted(prices_after)
