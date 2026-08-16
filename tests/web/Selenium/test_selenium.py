from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import Config
from tests.fixtures.selenium import driver


def test_selenium_login_and_search(driver:WebDriver, configs: Config):
    wait = WebDriverWait(driver=driver,timeout= 10, poll_frequency=0.1, ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
    #wait.until(EC.visibility_of_element_located())
    driver.get(configs.login_url)
    driver.find_element(by=By.CSS_SELECTOR, value="#content-desktop #user_email").send_keys(configs.email)
    driver.find_element(by=By.CSS_SELECTOR, value="#content-desktop #user_password").send_keys(configs.password)
    driver.find_element(by=By.CSS_SELECTOR, value="#content-desktop [value='Sign In']").click()
    driver.find_element(by=By.CSS_SELECTOR, value="#content-desktop .common-flash-success").is_displayed()
    target_project="python manufacture"
    driver.find_element(by=By.CSS_SELECTOR, value="#content-desktop #search").send_keys(target_project)
    driver.find_element(by=By.CSS_SELECTOR, value=f"#content-desktop [title='{target_project}']").click()
    #project_page_title=driver.find_element(by=By.CSS_SELECTOR, value=f"#content-desktop  .first [heading='{target_project}']").is_displayed()
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, f".breadcrumbs-page [title='{target_project}']"))

