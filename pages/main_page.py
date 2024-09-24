from base.base_class import Base
from pages.locators import Locators
from utils.constants import Constants


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    """Choosing an apple phone, using filters, adding and removing from the cart"""
    def select_apple(self):
        self.get_current_url()
        self.click_element(Locators.mobile_phones_button)
        self.assert_is(Locators.mobile_phones_title, Constants.mobile_phones_title)
        self.assert_url(Constants.mobile_phone_url)

        self.click_element(Locators.apple_checkbox)
        self.click_element(Locators.sort_by_price_button)
        self.click_element(Locators.sort_by_price_button)
        self.move_slider(Locators.slider_right_button, -70)

        name = self.get_text(Locators.first_product_name)
        price = self.get_text(Locators.first_product_price)

        self.click_element(Locators.first_product_add_to_cart_button)
        self.assert_is(Locators.modal_window_title_before_cart, Constants.modal_window_before_cart_title)
        self.click_element(Locators.proceed_to_checkout_button)
        self.assert_is(Locators.cart_title, Constants.cart_title)
        self.assert_url(Constants.cart_url)

        self.assert_is(Locators.name_product_in_cart, name)
        self.assert_is(Locators.total_price_in_cart, price)
        self.click_element(Locators.delete_product_in_cart_button)


    """Choosing a xiaomi phone using filters and checking the number of items on the page, adding and removing from the cart"""
    def select_xiaomi(self):
        self.get_current_url()
        self.click_element(Locators.mobile_phones_button)
        self.assert_is(Locators.mobile_phones_title, Constants.mobile_phones_title)
        self.assert_url(Constants.mobile_phone_url)

        self.click_element(Locators.xiaomi_select_button)

        self.click_element(Locators.compact_view_button)
        amount = "48"
        self.select_by_visible_text_in_dropdown(Locators.select_limit_item_on_page_dropdown, amount)
        amount_xiaomi = len(self.search_elements(Locators.xiaomi_products_button))
        assert amount == str(amount_xiaomi)

        name = self.get_text(Locators.first_product_name_compact_view)
        price = self.get_text(Locators.first_product_price_compact_view)

        self.click_element(Locators.first_product_add_to_cart_button_compact_view)
        self.assert_is(Locators.modal_window_title_before_cart, Constants.modal_window_before_cart_title)
        self.click_element(Locators.proceed_to_checkout_button)
        self.assert_is(Locators.cart_title, Constants.cart_title)
        self.assert_url(Constants.cart_url)

        self.assert_is(Locators.name_product_in_cart, name)
        self.assert_is(Locators.total_price_in_cart, price)
        self.click_element(Locators.delete_product_in_cart_button)
