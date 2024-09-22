from selenium.webdriver.common.by import By
from selenium.webdriver import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.locators import Locators


class MainPage(Base):

    def __init__(self, driver=None):
        super().__init__(driver)

    # Methods
    def select_apple(self):
        self.get_current_url()
        self.click_element(Locators.mobile_phones_button)
        self.assert_word(Locators.mobile_phones_title, "Мобильные телефоны")
        self.click_element(Locators.apple_checkbox)
        self.click_element(Locators.sort_by_price)

        # actoins = ActionChains(driver)
        # square = driver.find_element(By.XPATH, '//input[@id="id1"]')
        # actoins.click_and_hold(square).move_by_offset(150, 0).release().perform()