class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def transfer_account(self, amount, target_account):
        self.withdraw(amount)
        target_account.deposit(amount)
        return self.balance


# cuenta_ex = BankAccount(200)
# my_cuenta = BankAccount(300)
# print(my_cuenta.transfer_account(600, cuenta_ex))
# print(cuenta_ex.get_balance())
        