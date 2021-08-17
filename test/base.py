import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from utilities.devices import get_devices
import random


@pytest.mark.parametrize("udid , device_name , system_port", get_devices())
class AppiumBaseTest:
    driver = None
    appium_service = AppiumService()

    @pytest.fixture
    def set_up(self, udid , device_name , system_port):
        # get random port for appium server
        port_number = self.get_random_port()

        # start appium server programmatically
        self.start_server(port_number, device_name)

        # setup the driver
        self.driver = webdriver.Remote("http://127.0.0.1:" + str(port_number) + "/wd/hub", self.get_desired_capabilities(udid, device_name, system_port))
        self.driver.implicitly_wait(10)

        yield
        # tear down
        self.stop_server()

    def get_random_port(self):
        port_number = random.randint(1000, 9999)
        print(port_number)
        return port_number

    def get_desired_capabilities(self, udid, device_name, system_port):
        desired_cap = {
            "app": "app/General-Store.apk",
            "platformName": "Android",
            "udid": udid,
            "deviceName": device_name,
            "systemPort": int(system_port)
        }
        return desired_cap

    def start_server(self, port_number, device_name):
        print("\nStarting the appium server")
        self.appium_service.start(
            args=['--address', '127.0.0.1', '-p', str(port_number), '--log', './logs/' + device_name + '_appium.log'])

    def stop_server(self):
        self.appium_service.stop()
        print("\nStopping the appium server")