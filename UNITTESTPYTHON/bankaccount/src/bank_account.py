from src.exchange_api import get_exchange_rate, is_api_available
import os
from dotenv import load_dotenv


load_dotenv()

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self.log_transaction('Created account')
        
    def log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):

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