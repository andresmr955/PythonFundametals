class Persona:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def greet(self):
        print(f'Hello, I am {self.name}')

person = Persona("Andres", 26)
person.greet()

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def perimeter(self):
        total = 2 * (self.width + self.height)
        return total
    
rectangle = Rectangle(20, 10)
print(rectangle.perimeter())
print(rectangle.calculate_area())

class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    
    def speed_up(self):
        print("Car is speeding up")

    def stop_car(self):
        print("Car is stopping")

my_car = Car("Toyota", 2026, 200)
my_car.speed_up()
my_car.stop_car()

class Animal():
    def __init__(self, name, specie ):
        self.name = name 
        self.specie = specie

    def sound(self):
        print("Animal sound")

my_animal = Animal("Dog", "mammal")
my_animal.sound()

class BankAccount():
    def __init__(self, titular, amount):
        self.titular = titular
        self.amount = amount

    def deposit(self, amount_inserted):
        print(f'You are depositing {amount_inserted}')
        self.amount += amount_inserted
        print(f'new amount {self.amount}')
    
    def withdraw(self, amount_withdraw):
        if amount_withdraw <= 0:
            print("Withdrawal amount must be positive!")
        elif amount_withdraw > self.amount:
            print(f"Insufficient funds! You tried to withdraw {amount_withdraw}, but your balance is {self.amount}.")
        else:
            print(f'You are withdrawing {amount_withdraw}')
            self.amount -= amount_withdraw

    def show_balance(self):
        print(f'Your balance is {self.amount}')

my_account = BankAccount("Andres", 500)
my_account.deposit(200)
my_account.show_balance()
my_account.withdraw(400)
my_account.show_balance()        

## LEVEL 2

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def calculate_average(self):
        if len(self.grades) > 0:
            sum_total = sum(self.grades)
            average_total = sum_total / len(self.grades)
            print(f'The average grade of {self.name} is {average_total}')
        else:
            print("No grades available to calculate the average")

my_student = Student("Andres David")
my_student.grades = [40, 30, 60, 80, 90]
print(my_student.grades)
my_student.calculate_average()