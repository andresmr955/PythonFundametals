import os

class BankAccount:
    bank_name = "MyBank" # It is an attribute of the class and is shared by all instances
    """
    A class representing a bank account with a protected balance and a private account number.

    """
    def __init__(self, balance: float, account_number: float):

        """
        Initializes a new BankAccount instance.

        Parameters:
            balance (float): The initial balance of the account.
            account_number (str): The account number of the bank account.
        """
        self._balance = balance # Protected balance attribute
        self.__account_number = account_number # Private account number attribute
    
    @property
    def get_balance(self) -> float:
        """Returns the current balance of the account."""
        return self._balance
    
    def show_info(self) -> str:
        return f"Bank: {BankAccount.bank_name}"

    #protected method to update the balance
    # and register the transaction in a file called transactions.txt
    def _update_balance(self, amount: float):
        """
        Updates the balance of the account by a specified amount.

        Parameters:
            amount (float): The amount to be added (positive for deposit, negative for withdrawal).
        """
        self._balance += amount
        self.__register_transaction(amount)

    #class method to deposit and withdraw money from the account
    def deposit(self, amount):
        """
        Deposits a specified amount to the account and updates the balance.

        Parameters:
            amount (float): The amount to be deposited into the account.
        """
        self._update_balance(amount)
        print(f'Deposit of {amount} new balance is {self._balance}')

    def withdraw_balance(self, amount):

        """
        Withdraws a specified amount from the account if there are sufficient funds.

        Parameters:
            amount (float): The amount to be withdrawn from the account.

        Returns:
            str: A message indicating whether the withdrawal was successful or if there were insufficient funds.
        """
        if amount <= self._balance:
            self._update_balance(-amount)
            print(f'The withdraw {amount}.New balance is {self._balance}')
        else:
            print('Insufficient funds')
    
    #private method to register the transaction in a file
    # and check the current directory
    def __register_transaction(self, amount):
        # Check the current directory
        
        """
        Logs the transaction details to a file.

        Parameters:
            amount (float): The amount involved in the transaction.
        """
        # Open the file in append mode and log the transaction
        directory = '40.Privatesandprotected/exercise'
        os.makedirs(directory, exist_ok=True)  
        file_path = os.path.join(directory, 'transactions.txt')
        with open(file_path, 'a') as file:
            file.write(f'Transaction of {amount} registered for account number {self.__account_number}\n')

            

if __name__ == "__main__":
    account = BankAccount(1000, '123456789')
    account.deposit(500)
    account.withdraw_balance(200) 
    #print(account.get_balance()) # Accessing the protected balance attribute directly
    #account.__account_number
    # account.__account_number # This will raise an AttributeError because __account_number is private
