from selenium.webdriver.chrome.webdriver import WebDriver

from src.web.selenium_pages.login_page import LoginPage
from src.web.selenium_pages.project_page import ProjectPage
from src.web.selenium_pages.projects_page import ProjectsPage
from tests.conftest import Config
from tests.fixtures.selenium import driver as driver


def test_selenium_login_and_search(driver: WebDriver, configs: Config) -> None:
    target_project = "python manufacture"

    LoginPage(driver).open(configs.login_url).login(configs.email, configs.password)
    ProjectsPage(driver).wait_until_loaded().search_and_open_project(target_project)
    ProjectPage(driver).wait_until_opened(target_project)

