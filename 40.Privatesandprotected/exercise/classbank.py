import os
import json
from datetime import datetime
import logging

# Configura el logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    bank_name = "MyBank"  # Attribute shared by all instances
    
    def __init__(self, balance: float, account_number: float):
        self._balance = balance  # Protected balance attribute
        self.__account_number = account_number  # Private account number attribute
    
    @property
    def balance(self) -> float:
        """Returns the current balance of the account."""
        return self._balance
    
    def show_info(self) -> str:
        return f"Bank: {BankAccount.bank_name}"

    def _update_balance(self, amount: float):
        """
        Updates the balance of the account by a specified amount.
        Parameters:
            amount (float): The amount to be added (positive for deposit, negative for withdrawal).
        """
        self._balance += amount
        self.__register_transaction(amount)

    def deposit(self, amount):
        """Deposits a specified amount to the account and updates the balance."""
        self._update_balance(amount)
        logging.info(f'Deposit of {amount} new balance is {self._balance}')

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if there are sufficient funds.
        Parameters:
            amount (float): The amount to be withdrawn from the account.
        """
        if amount <= self._balance:
            self._update_balance(-amount)
            logging.info(f'The withdraw {amount}. New balance is {self._balance}')
        else:
            logging.warning('Insufficient funds')
    
    def __register_transaction(self, amount):
        """Logs the transaction details to a file."""
        directory = '40.Privatesandprotected/exercise/'
        os.makedirs(directory, exist_ok=True)  
        file_path = os.path.join(directory, 'transactions.txt')

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transactions = {'timestamp': timestamp, 'amount': amount, 'balance': self._balance}
        
        with open(file_path, 'a') as file:
            logging.info(f"Writing to the file at: {file_path}")
            file.write(json.dumps(transactions, indent=4))
            file.write('\n')

if __name__ == "__main__":
    account = BankAccount(1000, '123456789')
    account.deposit(500)
    account.withdraw(200)
