import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")
import unittest
import time
from src.comm_utility.ResultReporter import BaseTestCase
from src.comm_utility.Logger import print_log
from src.comm_utility.Constants import *
from src.comm_utility.ConfigParser import MoneyfyAppConfigGlobal, TRUE, FALSE
from src.moneyfy_actions.moneyfy_driver import MoneyfyDriver
from src.moneyfy_actions.screens.home_screen import MoneyfyHomeScreen


class TestMoneyfy(BaseTestCase):
    moneyfy = MoneyfyDriver().get_driver()
    moneyfy_home = MoneyfyHomeScreen(moneyfy)

    def test1_verify_change_of_currency(self):
        '''Test Case 1:  '''
        """ This method performs Test Case to Verify Moneyfy support in different currencies """

        try:
            print_log("launching moneeyfy and making ready")
            self.moneyfy_home.click_start_and_ready()
            print_log("dismissing advertisement")
            self.moneyfy_home.dismiss_advertisement()
            print_log("select settings")
            self.moneyfy_home.select_settings()
            print_log("select currency and change to INR")
            self.moneyfy_home.change_currency()
            print_log("navigate to home after changing currency")
            self.moneyfy_home.navigate_back_home()
            print_log("\n")
            count = 0
            expected_data = "Balance ₹0.00"
            actual_data = self.moneyfy_home.get_actual_currency_value()
            print_log("verify the currency change")
            if expected_data == actual_data:
                print_log("expected and actual data matched")
                count = count + 1
            else:
                print_log("!!!!actual data is not same as expected")

            if count == 1:
                self.verify(TRUE, "currency change on moneyfy verified successfully")
            else:
                self.verify(FALSE, "currency change not verified properly")
        finally:
            print_log("Entered finally")
            time.sleep(3)
    def test2_verify_expense_income_balance(self):
        '''Test Case 2:  '''
        """ This method performs Test Case to Verify added expense and income and remaining balance """

        try:
            print_log("launching moneyfy and making ready")
            self.moneyfy_home.click_start_and_ready()
            print_log("dismissing advertisement")
            self.moneyfy_home.dismiss_advertisement()
            print_log("select settings")
            self.moneyfy_home.select_settings()
            print_log("select currency and change to INR")
            self.moneyfy_home.change_currency()
            print_log("navigate to home after changing currency")
            self.moneyfy_home.navigate_back_home()
            print_log("adding expense")
            self.moneyfy_home.add_expence_amount()
            expected_expense = "₹500.00"
            actual_expense_added = self.moneyfy_home.get_expense_amount()
            print_log("\n")
            count = 0
            print_log("verify the currency change")
            if expected_expense == actual_expense_added:
                print_log("expected and actual data matched")
                count = count + 1
            else:
                print_log("!!!!actual data is not same as expected")
            print_log("adding income amount")
            self.moneyfy_home.add_income_amount()
            time.sleep(2)
            expected_income = "₹1000.00"
            actual_income_added = self.moneyfy_home.get_income_amount()
            print_log("\n")
            print_log("verify the currency change")
            if expected_income == actual_income_added:
                print_log("expected and actual data matched")
                count = count + 1
            else:
                print_log("!!!!actual data is not same as expected")
            print_log("calculating the expected balance")
            expected_balance = expected_income  - expected_expense
            actual_balance = self.moneyfy_home.get_balance_amount()
            print_log("\n")
            print_log("verify the remaining balance")
            if expected_balance == actual_balance:
                print_log("expected and actual data matched")
                count = count + 1
            else:
                print_log("!!!!actual data is not same as expected")

            if count == 3:
                self.verify(TRUE, "expense,income and balance on moneyfy verified successfully")
            else:
                self.verify(FALSE, "expense,income and balancenot verified properly")
        finally:
            print_log("Entered finally")
            time.sleep(3)



def main():
    TestCases = [
        'test1_verify_change_of_currency',
        'test2_verify_expense_income_balance'

    ]
    GlobalVar.Suite = unittest.TestSuite(map(TestMoneyfy, TestCases))
    unittest.TextTestRunner(verbosity=2).run(GlobalVar.Suite)



if __name__ == '__main__':
    main()
    print("Completed")
