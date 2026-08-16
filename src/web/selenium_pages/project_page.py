from typing import Self

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.web.selenium_pages.base_page import BasePage


class ProjectPage(BasePage):
    _PROJECT_HEADING = (By.CSS_SELECTOR, ".sticky-header h2")

    def __init__(self, driver: WebDriver, timeout: float = 10) -> None:
        super().__init__(driver, timeout)

    def wait_until_opened(self, project_name: str) -> Self:
        self._wait_until_visible(self._PROJECT_HEADING)
        self.wait.until(
            EC.text_to_be_present_in_element(
                self._PROJECT_HEADING,
                project_name,
            )
        )
        return self
