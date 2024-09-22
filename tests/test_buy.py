from pages.login_page import LoginPage
from pages.main_page import MainPage

def test_buy_product():
    login = LoginPage()
    login.open_page()
    login.authorization()

    main = MainPage(driver=login.driver)
    main.select_apple()