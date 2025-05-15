
import unittest
from dotenv import load_dotenv
from src.bank_account import BankAccount
from src.exchange_api import is_api_available
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
load_dotenv()

class BankAccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")     
        self.account_two = BankAccount(balance=2000)    
        self.api = os.getenv("BANXICO_API_KEY")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
    
    def _count_lines(self,filename):
        with open(filename, "r") as f:
            return len(f.readlines())
        
    def _check_lines_test(self, filename):
        with open(filename, 'r') as f:
             return f.readlines()
            
    def test_deposit_increase_balance(self):
          
          new_balance = self.account.deposit(410)
          assert new_balance == 1410

    def test_withdraw_decreases_balance(self):
         
         new_balance = self.account.withdraw(400)
         assert new_balance == 600
    
    @patch("src.bank_account.datetime")     
    def test_withdrawal_during_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.account.withdraw(100)
    
    def test_get_balance_returns_current_balance(self):
         balance = self.account.get_balance()
         assert balance == 1000

    # ----------------CHALLENGE-----------------------------
    def test_transfer_account_decreases_sender_balance(self):
        new_balance = self.account.transfer_account(500, self.account_two)
        self.assertEqual(new_balance, 500)
        self.assertEqual(self.account_two.balance, 2500)
    
    def test_transfer_account_error_insufficient_founds(self):
        with self.assertRaises(ValueError, msg="It should be a value error"):
            self.account.transfer_account(5000, self.account_two)

    def test_transaction_logs_each_transaction(self):
        self.account.deposit(678)
        assert os.path.exists("transaction_log.txt")

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(13448)
        assert self._count_lines(self.account.log_file) == 2 

    def test_check_lines_test(self):
        lines = self._check_lines_test(self.account.log_file)
        self.assertEqual(lines[0].strip(), "Created account")

    def test_method_error_handling(self):
        # 1. Store the initial balance (or other relevant values)
        initial_balance = self.account.balance
        
        # 2. Define the value you're going to test. 
        # In this case, a transfer amount that we know should fail
        transfer_amount = -41000  # Example of an invalid value for the test

        try:
            # 3. Try to execute the operation (for example, the transfer)
            self.account.transfer_account(transfer_amount, self.account_two)
        except ValueError:
            # 4. If an error is thrown (like ValueError), catch it here
            # This prevents the test from breaking and allows us to continue with validation
            pass

        # 5. Verify that the account balance **did not change** after the failed attempt
        self.assertEqual(self.account.balance, initial_balance, "The balance should remain the same after a failed transfer.")

        # 6. Check the log file to ensure the failed attempt was correctly logged
        lines = self._check_lines_test(self.account.log_file)  # Method to read lines from the log file
        found_log_message = False
        
        # 7. Create the expected message that should be found in the log
        expected_message = f"You have tried to transfer {transfer_amount}, but the funds are not enough your balance is: {self.account.balance}"
        
        # 8. Search for the expected message in the log lines
        for line in lines:
            if expected_message in line.strip():  # Compare the message without leading/trailing spaces
                found_log_message = True
                break  # Stop searching once we find the message

        # 9. Make sure the expected message **was found** in the log
        self.assertTrue(found_log_message, f"Log message not found '{expected_message}'")

    @unittest.skipUnless(is_api_available(os.getenv("BANXICO_API_KEY")), "API is not available")
    @patch('src.exchange_api.get_exchange_rate')
    def test_convert_to_usd(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 20
        cad_balance = self.account.convert_to_cad(self.api)
        self.assertAlmostEqual( cad_balance, 71.8) 
        #print(f' => {cad_balance}')
