from pages.login_page import LoginPage
from pages.main_page import MainPage

def test_buy_apple(set_up):
    login = LoginPage()
    login.open_page()
    login.authorization()

    main = MainPage(driver=login.driver)
    main.select_apple()
    main.close_browser()

def test_buy_xiaomi(set_up):
    login = LoginPage()
    login.open_page()
    login.authorization()

    main = MainPage(driver=login.driver)
    main.select_xiaomi()
    main.close_browser()