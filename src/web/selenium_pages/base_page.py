from typing import TypeAlias

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

Locator: TypeAlias = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: float = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(
            driver=driver,
            timeout=timeout,
            poll_frequency=0.1,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        )

    def _wait_until_visible(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _wait_until_clickable(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def _enter_text(self, locator: Locator, value: str) -> None:
        element = self._wait_until_clickable(locator)
        element.clear()
        element.send_keys(value)

    def _click(self, locator: Locator) -> None:
        self._wait_until_clickable(locator).click()
