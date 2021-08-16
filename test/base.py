import pytest
from appium import webdriver
# to start and stop appium from program
from appium.webdriver.appium_service import AppiumService
import os


class AppiumTest:
    desired_cap_pixel4 = {
        "app": "/Users/ashawami/workspace/Udemy/AppiumUdemy/AppiumProject/src/General-Store.apk",
        "platformName": "Android",
        "deviceName": "Pixel 4"
    }
    driver = None
    appium_service = AppiumService()

    @pytest.fixture
    def set_up(self):
        # self.start_emulator()
        # to start appium from program
        print("\nStarting the appium")
        # link for AppiumService - https://github.com/appium/python-client/blob/master/appium/webdriver/appium_service.py
        # link for appium_service.start() args -  https://appium.io/docs/en/writing-running-appium/server-args/
        self.appium_service.start(args=['--address', '127.0.0.1', '-p', str(4723), '--log', 'appium.log'])
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_cap_pixel4)
        self.driver.implicitly_wait(10)
        yield
        # to stop appium from program
        self.appium_service.stop()
        # self.stop_emulator()
        print("\nStopping the appium")

    def start_emulator(self):
        emulator = "emulator @Pixel_4"
        os.system(emulator)

    def stop_emulator(self):
        emulator = "adb -s emulator-5554 emu kill"
        os.system(emulator)

