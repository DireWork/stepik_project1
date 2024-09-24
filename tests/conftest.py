import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.constants import Constants

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    path_chrome = Service(Constants.chromedriver_path)
    driver = webdriver.Chrome(service=path_chrome, options=options)

    driver.maximize_window()
    driver.get(Constants.base_url)

    yield driver

    driver.quit()
    print("Browser is closed")