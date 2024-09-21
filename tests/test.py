import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--no-sandbox")
# options.add_argument("--headless")
path_chrome = Service("C:\\Users\\kosty\\OneDrive\\Desktop\\qa courses\\SELENIUM\\chromedriver.exe")
driver = webdriver.Chrome(service=path_chrome, options=options)
driver.get("https://www.pleer.ru/")
driver.maximize_window()