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
        name = self.get_text(Locators.first_product_name)
        price = self.get_text(Locators.first_product_price)
        self.click_element(Locators.first_product_add_to_cart)
        self.assert_word(Locators.title_modal_window, 'Корзина')
        self.click_element(Locators.btn_proceed_to_checkout)
        self.assert_word(Locators.name_product_in_cart, name)
        self.assert_word(Locators.total_price_in_cart, price)
        self.click_element(Locators.delete_product_in_cart)
