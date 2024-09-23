import time

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
        self.click_element(Locators.sort_by_price)
        self.move_slider(Locators.slider2 , -70)