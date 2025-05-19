

from exchange_api import get_exchange_rate
import os
from datetime import datetime
from dotenv import load_dotenv
from exceptions import WithdrawalDayTimeRestrictionError, WithdrawalTimeRestrictionError

load_dotenv()

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self.log_transaction('Created account')
        
    def log_transaction(self, message):

        """
        Write a message

        >>> import os
        >>> temp_file = "temp_log.txt"
        >>> account = BankAccount(log_file=temp_file)
        >>> account.log_transaction("Test message")
        >>> with open(temp_file) as f:
        ...    print(f.read().strip())
        Created account
        Test message
        >>> os.remove(temp_file)
        """
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        """
        >>> account = BankAccount()
        >>> account.deposit(1000)
        1000

        >>> account = BankAccount()
        >>> account.deposit(-400)
        Traceback (most recent call last):
            ...
        ValueError: Deposit amount must be positive
        """

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):


        """
        >>> account = BankAccount(1000)
        >>> account.withdraw(500)
        500


        >>> account.withdraw(2000)
        Traceback (most recent call last):
            ...
        ValueError: Insufficient funds

        >>> account.withdraw(-2000)
        Traceback (most recent call last):
            ...
        ValueError: It is not possible

        """
        now = datetime.now()
    
        if now.isoweekday() in [6,7]:
            raise WithdrawalDayTimeRestrictionError("Withdrawal are only allowed in business days") 

        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawal are only allowed from 8am to 5pm")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds") 
        elif amount < 0: 
            raise ValueError("It is not possible")
        else:
            self.balance -= amount
            self.log_transaction(f"Withdraw {amount}. New balance: {self.balance}")
        
        return self.balance
    
    def get_balance(self):
        self.log_transaction(f"Your current balance is {self.balance}")
        return self.balance
    
    def transfer_account(self, amount, target_account):
        try: 
            self.withdraw(amount)
            target_account.deposit(amount)
            self.log_transaction(f"You have transferred {amount}, New balance is: {self.balance}")
            
        except ValueError as e:
            
            self.log_transaction(f"You have tried to transfer {amount}, but the funds are not enough your balance is: {self.balance}")
            raise 
        return self.balance
    def convert_to_cad(self, api):

        if not api_key:
            print("Error: Banxico API key is not set in environment variable BANXICO_API_KEY")
            self.log_transaction("Failed to convert balance to CAD: API key not found.")
            return None
        
        exchange_rate = get_exchange_rate(api_key)
        if exchange_rate:
            return round(self.balance / exchange_rate, 1)
        else: 
            self.log_transaction("Failed to convert balance to CAD.")
            return None
        
cuenta_ex = BankAccount(200)
# my_cuenta = BankAccount(300)
# print(my_cuenta.transfer_account(600, cuenta_ex))
# print(cuenta_ex.get_balance())
api_key = os.getenv("BANXICO_API_KEY")

result = cuenta_ex.convert_to_cad(api_key)

#print(result)

