from selenium.webdriver.common.by import By
from selenium.webdriver import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators 
    product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    product_3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//a[@data-test="shopping-cart-link"]'
    main_word = '//span[@data-test="title"]'
    menu_button = '//button[@id="react-burger-menu-btn"]'
    about_button = '//a[@id="about_sidebar_link"]'


    # Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
    def get_product_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))
    def get_product_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_3)))
    
    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.about_button)))
    

    # actions
    def click_product_1(self):
        self.get_product_1().click()
        print("click product 1")
    def click_product_2(self):
        self.get_product_2().click()
        print("click product 2")
    def click_product_3(self):
        self.get_product_3().click()
        print("click product 3")

    def click_cart(self):
        self.get_cart().click()
        print("click cart button")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("click menu button")

    def click_about_button(self):
        self.get_about_button().click()
        print("click about button")


    # Methods
    def select_product_1(self):
        self.get_current_url()
        self.assert_word(self.get_main_word(), "Products")
        self.click_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.assert_word(self.get_main_word(), "Products")
        self.click_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.assert_word(self.get_main_word(), "Products")
        self.click_product_3()
        self.click_cart()

    def select_about(self):
        self.get_current_url()
        self.assert_word(self.get_main_word(), "Products")
        self.click_menu_button()
        self.click_about_button()
        self.assert_url("https://saucelabs.com/")
        self.get_screenshot()
