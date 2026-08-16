import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0)
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()