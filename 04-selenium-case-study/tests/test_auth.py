from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import LOCKED_OUT_USER, PASSWORD, STANDARD_USER


def test_valid_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_until_loaded()

    assert "/inventory.html" in driver.current_url
    assert inventory_page.inventory_visible


def test_locked_out_user_is_rejected(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    assert "Sorry, this user has been locked out." in login_page.error_message
    assert "/inventory.html" not in driver.current_url
    assert login_page.login_form_visible


def test_logout_blocks_direct_inventory_access(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_until_loaded()
    inventory_page.logout()
    login_page.visible(login_page.USERNAME)

    driver.get(inventory_page.INVENTORY_URL)

    assert login_page.login_form_visible
    assert "You can only access '/inventory.html' when you are logged in." in login_page.error_message
    assert "/inventory.html" not in driver.current_url
    assert not inventory_page.inventory_visible
