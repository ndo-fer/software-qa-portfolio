from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    BASE_URL = "https://www.saucedemo.com/"

    USERNAME = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-test="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR = (By.CSS_SELECTOR, '[data-test="error"]')

    def load(self) -> None:
        self.open(self.BASE_URL)
        self.visible(self.USERNAME)

    def login(self, username: str, password: str) -> None:
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    @property
    def error_message(self) -> str:
        return self.text(self.ERROR)

    @property
    def login_form_visible(self) -> bool:
        return self.is_visible(self.USERNAME)
