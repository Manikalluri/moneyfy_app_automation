import time

from appium import webdriver
import os

def PATH(p: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', p))

from src.comm_utility.ConfigParser import MoneyfyAppConfigGlobal

appium_server_ip = MoneyfyAppConfigGlobal.AppiumHost_IP

class Moneyfy:

    driver = None
    user_name = None
    password = None
    server_ip = None

    def __init__(self, driver, user_name, password, server_ip):
        self.driver = driver
        self.user_name = user_name
        self.password = password
        self.server_ip = server_ip

class MoneyfyDriver(object):

    driver = None

    def __init__(self):

        desired_caps = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceID='RZCT31DB65X',
            appActivity='com.monefy.app.lite.authentication.AuthenticationActivity',
            appPackage='com.monefy.app.lite',
            noReset='true',
            newCommandTimeout = 60,
            app=PATH('../tools/apps/monyfy.apk')
        )

        if MoneyfyDriver.driver is None:
            for x in range(2):
                try:
                    MoneyfyDriver.driver  = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
                    MoneyfyDriver.driver = self.driver
                    MoneyfyDriver.driver.implicitly_wait(10)
                    time.sleep(1)
                    break
                except Exception as e:
                    print (e)
                    time.sleep(1)
                    continue
        else:
            print ("Moneyfy driver already exist")

        if MoneyfyDriver.driver is None:
            print ("Failed to connect to Moneyfy")
            raise Exception("Failed to connect to Moneyfy")

    @staticmethod
    def get_driver():
        if MoneyfyDriver.driver is None:
            MoneyfyDriver()
        return MoneyfyDriver.driver
