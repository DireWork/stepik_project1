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
    apple_checkbox = '//input[@id="mfilter-opts-attribs-86-manufacturers-45"]//..//..//label'
    sort_by_price = '//span[text()="Цена "]'