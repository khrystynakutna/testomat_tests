from typing import Self

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.web.selenium_pages.base_page import BasePage


class LoginPage(BasePage):
    _EMAIL_INPUT = (By.CSS_SELECTOR, "#content-desktop #user_email")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#content-desktop #user_password")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#content-desktop [value='Sign In']")

    def __init__(self, driver: WebDriver, timeout: float = 10) -> None:
        super().__init__(driver, timeout)

    def open(self, login_url: str) -> Self:
        self.driver.get(login_url)
        self._wait_until_visible(self._EMAIL_INPUT)
        return self

    def login(self, email: str, password: str) -> None:
        self._enter_text(self._EMAIL_INPUT, email)
        self._enter_text(self._PASSWORD_INPUT, password)
        self._click(self._SIGN_IN_BUTTON)
