from base.base_class import Base
from pages.locators import Locators


class MainPage(Base):

    def __init__(self, driver=None):
        super().__init__(driver)

    # Methods
    def select_apple(self):
        self.get_current_url()
        self.click_element(Locators.mobile_phones_button)
        self.assert_is(Locators.mobile_phones_title, 'Мобильные телефоны')
        self.assert_url('https://mobilguru.by/mobilnye-telefony')

        self.click_element(Locators.apple_checkbox)
        self.click_element(Locators.sort_by_price)
        self.click_element(Locators.sort_by_price)
        self.move_slider(Locators.slider2 , -70)

        name = self.get_text(Locators.first_product_name)
        price = self.get_text(Locators.first_product_price)

        self.click_element(Locators.first_product_add_to_cart)
        self.assert_is(Locators.title_modal_window, 'Корзина')
        self.click_element(Locators.button_proceed_to_checkout)
        self.assert_is(Locators.cart_title, 'Оформление заказа')
        self.assert_url('https://mobilguru.by/index.php?route=checkout/uni_checkout')

        self.assert_is(Locators.name_product_in_cart, name)
        self.assert_is(Locators.total_price_in_cart, price)
        self.click_element(Locators.delete_product_in_cart)

    def select_xiaomi(self):
        self.get_current_url()
        self.click_element(Locators.mobile_phones_button)
        self.assert_is(Locators.mobile_phones_title, 'Мобильные телефоны')
        self.assert_url('https://mobilguru.by/mobilnye-telefony')

        self.click_element(Locators.xiaomi_select_button)

        self.click_element(Locators.compact_view)
        amount = "48"
        self.select_by_visible_text_in_dropdown(Locators.select_limit_item_on_page,amount)
        amount_xiaomi = len(self.search_elements(Locators.xiaomi_products))
        assert amount == str(amount_xiaomi)

        name = self.get_text(Locators.first_product_name_compact_view)
        price = self.get_text(Locators.first_product_price_compact_view)

        self.click_element(Locators.first_product_add_to_cart_compact_view)
        self.assert_is(Locators.title_modal_window, 'Корзина')
        self.click_element(Locators.button_proceed_to_checkout)
        self.assert_is(Locators.cart_title, 'Оформление заказа')
        self.assert_url('https://mobilguru.by/index.php?route=checkout/uni_checkout')

        self.assert_is(Locators.name_product_in_cart, name)
        self.assert_is(Locators.total_price_in_cart, price)
        self.click_element(Locators.delete_product_in_cart)
