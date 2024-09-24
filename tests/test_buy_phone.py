from pages.login_page import LoginPage
from pages.main_page import MainPage

def test_buy_apple(driver):
    login = LoginPage(driver)
    login.authorization()

    main = MainPage(driver)
    main.select_apple()

def test_buy_xiaomi(driver):
    login = LoginPage(driver)
    login.authorization()

    main = MainPage(driver)
    main.select_xiaomi()