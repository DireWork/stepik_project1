from utils.constants import Constants
from selenium.webdriver.common.by import By

class Locators:

    """LOGIN PAGE"""
    account_button = By.ID, 'account'
    authorization_button = By.XPATH, '//a[text()="Авторизация"]'
    login_input = By.ID, 'input-email'
    password_input = By.ID, 'input-password'
    login_button = By.XPATH, '//button[@type="submit"]'
    user_name = By.XPATH, f'//span[text()="{Constants.user_name}"]'

    """MAIN PAGE"""
    mobile_phones_button = By.XPATH, '//a[@href="https://mobilguru.by/mobilnye-telefony"]'
    mobile_phones_title = By.XPATH, '//h1[text()="Мобильные телефоны"]'
    apple_checkbox = By.XPATH, '//input[@id="mfilter-opts-attribs-86-manufacturers-45"]'
    sort_by_price_button = By.XPATH, '//span[text()="Цена "]'
    slider_right_button = By.XPATH, '//*[@id="mfilter-price-slider"]/span[2]'
    first_product_name = By.XPATH, '(//div[@class="product-thumb__caption"])[1]/a'
    first_product_price = By.XPATH, '(//div[@class="product-thumb__caption"])[1]/div[4]'
    first_product_add_to_cart_button = By.XPATH, '(//div[@class="product-thumb__caption"])[1]/div[5]/button[1]'
    modal_window_title_before_cart = By.XPATH, '//h4[@class="modal-title"]'
    proceed_to_checkout_button = By.XPATH, '(//a[text()="Перейти к оформлению заказа"])[2]'
    name_product_in_cart = By.XPATH, '//div[@class="checkout-cart__name"]/a'
    total_price_in_cart = By.XPATH,  '//span[@class="total"]'
    delete_product_in_cart_button = By.XPATH, '//i[@title="Удалить"]'
    xiaomi_select_button = By.XPATH, '//a[@href="https://mobilguru.by/mobilnye-telefony/xiaomi-1"]/span'
    compact_view_button = By.ID, 'compact-view'
    select_limit_item_on_page_dropdown = By.ID, 'input-limit'
    xiaomi_products_button = (By.XPATH, '//div[contains(@class, "uni-item")]')
    first_product_name_compact_view = By.XPATH, '(//div[@class="product-thumb__caption"])[1]/a'
    first_product_price_compact_view = By.XPATH, '(//div[@class="product-thumb__caption"])[1]/div[3]'
    first_product_add_to_cart_button_compact_view = By.XPATH, '(//div[@class="product-thumb__caption"])[1]/div[4]/button[1]'
    cart_title = By.XPATH, '//h1[text()="Оформление заказа"]'