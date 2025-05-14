import unittest
from test_bank_account import BankAccountTest

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTest("test_get_balance"))
    suite.addTest(BankAccountTest("test_withdraw"))
    
    
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite()) 