import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import random

@pytest.mark.parametrize("udid , deviceName , systemPort" , [("emulator-5554" , "Pixel 4" , "8201") , ("emulator-5556" , "Pixel" , "8202")])
def test_set_up(udid , deviceName , systemPort):
    desired_cap_pixel = {
        "app": "/Users/ashawami/workspace/Udemy/AppiumUdemy/AppiumProject/src/General-Store.apk",
        "platformName": "Android",
        "udid": udid,
        "deviceName": deviceName,
        "systemPort": int(systemPort)
    }

    driver = None

    port_number = random.randint(1000, 9999)
    print(port_number)
    appium_service = AppiumService()
    print("\nStarting the appium")
    appium_service.start(args=['--address', '127.0.0.1', '-p', str(port_number), '--log', deviceName + '_appium.log'])
    driver = webdriver.Remote("http://127.0.0.1:" + str(port_number) +"/wd/hub", desired_cap_pixel)
    driver.implicitly_wait(10)

    # actions
    driver.find_element_by_id("com.androidsample.generalstore:id/radioFemale").click()
    driver.find_element_by_id("com.androidsample.generalstore:id/nameField").send_keys("Steve");
    driver.hide_keyboard()
    driver.find_element_by_id("com.androidsample.generalstore:id/btnLetsShop").click()

    #teardown
    appium_service.stop()
    print("\nStopping the appium")

















# def test_set_up():
#     desired_cap_pixel = {
#         "app": "/Users/ashawami/workspace/Udemy/AppiumUdemy/AppiumProject/src/General-Store.apk",
#         "platformName": "Android",
#         "udid": "emulator-5554",
#         "deviceName": "Pixel 4",
#         "systemPort": 8201
#     }
#     driver = None
#     appium_service = AppiumService()
#     print("\nStarting the appium")
#     appium_service.start(args=['--address', '127.0.0.1', '-p', str(4723), '--log', 'appium.log'])
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap_pixel)
#     driver.implicitly_wait(10)
#     appium_service.stop()
#     print("\nStopping the appium")