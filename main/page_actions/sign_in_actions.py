from appium import webdriver
from ..page_object.sign_in_objects import SignInObjects


class SignInActions(SignInObjects):
    def __init__(self, driver: webdriver):
        super().__init__()
        self.driver = driver

    def sign_in(self, username):
        self.driver.find_element_by_id(self.female_radio_checkout).click()
        self.driver.find_element_by_id(self.username).send_keys(username)
        self.driver.hide_keyboard()
        self.driver.find_element_by_id(self.lets_shop_button).click()
