from base.base_class import Base
from pages.locators import Locators
from utils.constants import Constants

class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    """Authorizes the user on the page using the specified username and password"""
    def authorization(self):
        self.get_current_url()
        self.click_element(Locators.account_button)
        self.click_element(Locators.authorization_button)
        self.send_text(Locators.login_input, Constants.login)
        self.send_text(Locators.password_input, Constants.password)
        self.click_element(Locators.login_button)
        self.get_current_url()
        self.assert_is(Locators.account_button, Constants.user_name)
        print("Success login")