from pages.login_page import LoginPage
login = LoginPage()

def test_buy_product():
    login.open_page()
    login.authorization()