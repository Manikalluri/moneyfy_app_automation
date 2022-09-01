import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from src.comm_utility.Logger import print_log

'''this class contains page objects and action methods'''


class MoneyfyHomeScreen:
    '''Page Locators'''
    Navigate_back = (MobileBy.XPATH, "//*[@content-desc='Close navigation']")
    start_ready_monefy = (MobileBy.ID, 'com.monefy.app.lite:id/buttonContinue')
    dismiss_ad = (MobileBy.ID, 'com.monefy.app.lite:id/buttonClose')
    threedotmenu = (MobileBy.ID, 'com.monefy.app.lite:id/overflow')
    settings = (MobileBy.ID, 'com.monefy.app.lite:id/settings_imagebutton')
    currency = (MobileBy.ID, 'com.monefy.app.lite:id/currency_name')
    search_country = (MobileBy.ID, 'com.monefy.app.lite:id/search_src_text')
    select_india = (MobileBy.XPATH, "//*[@text='Indian Rupee']")
    currency_value = (MobileBy.ID, 'com.monefy.app.lite:id/balance_amount')
    add_expense = (MobileBy.ID, 'com.monefy.app.lite:id/expense_button')
    add_amount = (MobileBy.ID, 'com.monefy.app.lite:id/amount_text')
    notes = (MobileBy.ID, 'com.monefy.app.lite:id/textViewNote')
    choose_catgeory = (MobileBy.ID, 'com.monefy.app.lite:id/keyboard_action_button')
    select_car = (MobileBy.XPATH, "//*[@text='Car']")
    snack_bar = (MobileBy.ID, 'com.monefy.app.lite:id/snackbar_text')
    expense_amount = (MobileBy.ID, 'com.monefy.app.lite:id/expense_amount_text')
    income_amount = (MobileBy.ID, 'com.monefy.app.lite:id/income_amount_text')
    balance_amount = (MobileBy.ID, 'com.monefy.app.lite:id/balance_amount')
    add_income = (MobileBy.ID, 'com.monefy.app.lite:id/income_button')
    select_salary = (MobileBy.XPATH, "//*[@text='Salary']")








    def __init__(self, driver):
        self.androiddriver = driver


    def click_start_and_ready(self):
        element = self.androiddriver.find_element(*MoneyfyHomeScreen.start_ready_monefy)
        try:
            if element.is_displayed():
                print_log("clicking on start,amaze and ready")
                element.click()
                element.click()
                element.click()
        except:
            print("start and ready button not found, continue next action")

    def dismiss_advertisement(self):
        self.androiddriver.find_element(*MoneyfyHomeScreen.dismiss_ad).click()

    def select_settings(self):
        self.androiddriver.find_element(*MoneyfyHomeScreen.threedotmenu).click()
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.settings).click()

    def change_currency(self):
        self.androiddriver.find_element(*MoneyfyHomeScreen.currency).click()
        time.sleep(2)
        print_log("selecting indian rupee")
        self.androiddriver.find_element(*MoneyfyHomeScreen.search_country).send_keys("india")
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.select_india).click()
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.Navigate_back).click()

    def navigate_back_home(self):
        self.androiddriver.find_element(*MoneyfyHomeScreen.Navigate_back).click()

    def get_actual_currency_value(self):
        return self.androiddriver.find_element(*MoneyfyHomeScreen.currency_value).get_attribute("text")

    def add_expence_amount(self):
        self.androiddriver.find_element(*MoneyfyHomeScreen.add_expense)
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.add_amount).send_keys("500")
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.notes).send_keys("Car Fuel")
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.choose_catgeory).click()
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.select_car).click()

    def add_income_amount(self):
        self.androiddriver.find_element(*MoneyfyHomeScreen.add_income)
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.add_amount).send_keys("1000")
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.notes).send_keys("Salary")
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.choose_catgeory).click()
        time.sleep(2)
        self.androiddriver.find_element(*MoneyfyHomeScreen.select_salary).click()

    def get_expense_amount(self):
        return self.androiddriver.find_element(*MoneyfyHomeScreen.expense_amount).get_attribute("text")

    def get_income_amount(self):
        return self.androiddriver.find_element(*MoneyfyHomeScreen.income_amount).get_attribute("text")

    def get_balance_amount(self):
        return self.androiddriver.find_element(*MoneyfyHomeScreen.balance_amount).get_attribute("text")

