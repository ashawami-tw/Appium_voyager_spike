from appium import webdriver

class SignIn:
    def __init__(self, driver:webdriver):
        self.driver = driver

    def sign_in(self , username):
        self.driver.find_element_by_id("com.androidsample.generalstore:id/radioFemale").click()
        self.driver.find_element_by_id("com.androidsample.generalstore:id/nameField").send_keys(username);
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.androidsample.generalstore:id/btnLetsShop").click()