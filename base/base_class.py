import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from utils.constants import Constants

class Base:

    def __init__(self, driver=None):
        self.driver = driver
        if self.driver is None:
            self.options = webdriver.ChromeOptions()
            self.options.add_experimental_option('detach', True)
            self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
            self.options.add_argument("--no-sandbox")
            self.path_chrome = Service("C:\\Users\\kosty\\OneDrive\\Desktop\\qa courses\\SELENIUM\\chromedriver.exe")
            self.driver = webdriver.Chrome(service=self.path_chrome, options=self.options)

    """Method open browser"""
    def open_page(self):
        self.driver.get(Constants.url)
        self.driver.maximize_window()

    """Method close browser"""
    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
        print("Browser closed")

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Method assert word"""
    def assert_word(self, locator, result):
        element = self.check_element_presence(locator)
        assert element.text == result
        print("good assert word")

    """Method screenshot"""
    def get_screenshot(self, sort):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(f"D:\\Projects\\testProject\\screen\\{name_screenshot}")
        print(f"Screenshot {sort} {name_screenshot} done")

    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("good value URL")

    """Method check element presence"""
    def check_element_presence(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            return element
        except:
            self.get_screenshot("error")
            print("Error: element_presence")
            raise

    """Method click element"""
    def click_element(self, locator):
        try:
            element = self.check_element_presence(locator)
            element.click()
        except:
            self.get_screenshot("error")
            print("Error: click_element")
            raise

    def send_text(self, locator , text):
        try:
            element = self.check_element_presence(locator)
            element.send_keys(text)
        except:
            self.get_screenshot("error")
            print("Error: send_keys")
            raise