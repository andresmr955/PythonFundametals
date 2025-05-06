import unittest
import os
from classbank import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        print("Setting up the test case...")
        self.account = BankAccount(1000.0, "123456789")

    def tearDown(self):
        print("Tearing down the test case...   cleaning up...")
        if os.path.exists('40.Privatesandprotected/exercise/transactions.txt'):
            os.remove('40.Privatesandprotected/exercise/transactions.txt')

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.0)
    
    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        self.account.withdraw(600)
        self.assertEqual(self.account.balance, 400)

    def test_transaction_file_created(self):
        self.account.deposit(100) 
        self.assertTrue(os.path.exists('40.Privatesandprotected/exercise/transactions.txt'))

if __name__ == "__main__":
    unittest.main()