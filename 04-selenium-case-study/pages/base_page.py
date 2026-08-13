from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Reusable explicit-wait and WebDriver interaction primitives."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def all_present(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        self.clickable(locator).click()

    def type_text(self, locator: tuple[str, str], value: str) -> None:
        element = self.visible(locator)
        element.clear()
        element.send_keys(value)

    def text(self, locator: tuple[str, str]) -> str:
        return self.visible(locator).text

    def wait_for_url_contains(self, fragment: str) -> bool:
        return self.wait.until(EC.url_contains(fragment))

    def is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            self.visible(locator)
        except TimeoutException:
            return False
        return True

    def is_absent(self, locator: tuple[str, str]) -> bool:
        return self.wait.until(EC.invisibility_of_element_located(locator))
