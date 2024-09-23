class Locators:

    """LOGIN PAGE"""
    account_button = '//div[@id="account"]'
    authorization_button = '//a[text()="Авторизация"]'
    login = '//input[@id="input-email"]'
    password = '//input[@id="input-password"]'
    login_button = '//button[@type="submit"]'
    user_name = '//span[text()="Иван"]'

    """MAIN PAGE"""
    mobile_phones_button = '//a[@href="https://mobilguru.by/mobilnye-telefony"]'
    mobile_phones_title = '//h1[text()="Мобильные телефоны"]'
    apple_checkbox = '//input[@id="mfilter-opts-attribs-86-manufacturers-45"]'
    sort_by_price = '//span[text()="Цена "]'
    slider2 = '//*[@id="mfilter-price-slider"]/span[2]'
    first_product_name = '(//div[@class="product-thumb__caption"])[1]/a'
    first_product_price = '(//div[@class="product-thumb__caption"])[1]/div[4]'
    first_product_add_to_cart = '(//div[@class="product-thumb__caption"])[1]/div[5]/button[1]'
    title_modal_window = '//h4[@class="modal-title"]'
    btn_proceed_to_checkout = '(//a[text()="Перейти к оформлению заказа"])[2]'
    name_product_in_cart = '//div[@class="checkout-cart__name"]/a'
    total_price_in_cart = '//span[@class="total"]'
    delete_product_in_cart = '//i[@title="Удалить"]'