##Class Bank

class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.status = True

    def deposit(self, amount):
        if self.status:
            self.balance += amount
            print(self.balance)
        else:
            print("We can not deposit, account is inactive")

    def withdraw(self, amount):
        if not self.status:
            print("We can not withdraw, account is inactive")
        else:    
            if amount <= self.balance:
                self.balance -= amount
                print(f'From the account we have done a withdraw {amount} and the balance is {self.balance}') 
            else:     
                print("You have not enough money")

    def deactivate_account(self):
        if self.status:
            self.status = False
            print("The account has been deactivated")
        else:
            print("The account is already deactivated")   

    def activate_account(self):
        if not self.status:
            self.status = True
            print("The account has been activated")
        else:
            print("The account is already activated")  

first_user = BankAccount("Andres", 1000)
second_user = BankAccount("David", 3000)

first_user.deposit(1000)
first_user.deactivate_account()
first_user.deactivate_account()
first_user.deposit(1000)
first_user.activate_account()
first_user.activate_account()
first_user.deposit(500)


second_user.withdraw(1000)
second_user.deactivate_account()
second_user.deactivate_account()
second_user.withdraw(1000)
second_user.activate_account()
first_user.activate_account()
second_user.withdraw(500)
second_user.withdraw(8000000)


'''
class Person: 
    ##Here we define the attributes
    #This is the constructor
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def greet(self):
        print(f'Hello, my name is {self.name} and my age is {self.age}')
    

person_a = Person("Ana", 8)
person_b = Person("Luis", 25)

#This is the method
person_a.greet()
person_b.greet()
'''