from typing import Self

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.web.selenium_pages.base_page import BasePage


class ProjectsPage(BasePage):
    _SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, "#content-desktop .common-flash-success")
    _SEARCH_INPUT = (By.CSS_SELECTOR, "#content-desktop #search")
    _SUCCESS_MESSAGE = "Signed in successfully"

    def __init__(self, driver: WebDriver, timeout: float = 10) -> None:
        super().__init__(driver, timeout)

    def wait_until_loaded(self) -> Self:
        self._wait_until_visible(self._SUCCESS_NOTIFICATION)
        self.wait.until(
            EC.text_to_be_present_in_element(
                self._SUCCESS_NOTIFICATION,
                self._SUCCESS_MESSAGE,
            )
        )
        self._wait_until_visible(self._SEARCH_INPUT)
        return self

    def search_and_open_project(self, project_name: str) -> None:
        project_link = (
            By.CSS_SELECTOR,
            f"#content-desktop [title='{project_name}']",
        )
        self._enter_text(self._SEARCH_INPUT, project_name)
        self._click(project_link)
