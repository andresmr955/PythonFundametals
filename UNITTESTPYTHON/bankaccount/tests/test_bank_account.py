import unittest

from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)     
        self.account_two = BankAccount(balance=2000)     
    def test_deposit(self):
          
          new_balance = self.account.deposit(410)
          assert new_balance == 1410

    def test_withdraw(self):
         
         new_balance = self.account.withdraw(400)
         assert new_balance == 600

    def test_get_balance(self):
         
         balance = self.account.get_balance()
         assert balance == 1000

    # ----------------CHALLANGE-----------------------------
    def test_transfer_account(self):
        new_balance = self.account.transfer_account(500, self.account_two)
        self.assertEqual(new_balance, 500)
        self.assertEqual(self.account_two.balance, 2500)
    
    def test_transfer_account_error(self):
         with self.assertRaises(ValueError, msg="It should be a value error"):
            self.account.transfer_account(5000, self.account_two)
