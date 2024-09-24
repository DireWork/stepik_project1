import datetime
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from utils.constants import Constants

class Base:

    def __init__(self, driver=None):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Method assert word"""
    def assert_is(self, locator, expected_text):
        element = self.check_element_presence(locator)
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"

    """Method screenshot"""
    def get_screenshot(self, sort):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(Constants.screen_path + name_screenshot)
        print(f"Screenshot {sort} {name_screenshot} done")

    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("good value URL")

    """Method check element presence"""
    def check_element_presence(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
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
            time.sleep(1)
        except:
            self.get_screenshot("error")
            print("Error: click_element")
            raise

    """Method send text to element"""
    def send_text(self, locator , text):
        try:
            element = self.check_element_presence(locator)
            element.send_keys(text)
        except:
            self.get_screenshot("error")
            print("Error: send_keys")
            raise

    """Method move slider"""
    def move_slider(self, locator, to_position):
        try:
            element = self.check_element_presence(locator)
            action = ActionChains(self.driver)
            action.click_and_hold(element).move_by_offset(to_position, 0).release().perform()
            time.sleep(1)
        except:
            self.get_screenshot("error")
            print("Error: move_slider")
            raise

    """Method get text from element"""
    def get_text(self, locator):
        try:
            value = self.check_element_presence(locator).text
            return value
        except:
            self.get_screenshot("error")
            print("Error: get_text")
            raise

    """Method select in dropdown"""
    def select_by_visible_text_in_dropdown(self, locator, text):
        try:
            element = self.check_element_presence(locator)
            select = Select(element)
            select.select_by_visible_text(text)
            time.sleep(1)
        except:
            self.get_screenshot("error")
            print("Error: select_by_visible_text_in_dropdown")
            raise

    """Method find elements"""
    def search_elements(self, locator):
        try:
            elements = self.driver.find_elements(*locator)
            return elements
        except:
            self.get_screenshot("error")
            print("Error: search_elements")
            raise