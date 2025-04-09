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

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.read = False
    
    def mark_read(self):
        self.read = True
        print(f'You have marked {self.title} as read')

    def show_status(self):
        if self.read:
            print(f'{self.title} by {self.author} has already been read')
        else:
            print(f'{self.title} by {self.author} has not been read yet')

my_book = Book("The little prince", "Andres")
my_book.mark_read()


class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete_task(self):
        self.completed = True
    
    def show_status(self):
        if self.completed:
            print(f'The task status is {self.completed}, completed')
        else: 
            print(f'The task status is not completed')

my_task = Task("Finish 20 classes")
my_task.complete_task()
my_task.show_status()


class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = {}

    def sell_units(self, item, quantity):
        if item not in self.stock:
            print(f'Item {item} is not in stock')
            return 
        
        if quantity <=  0:
            print("It is not possible to sell something less or equal to 0")   

        if quantity <= self.stock[item]:
            self.stock[item] -= quantity
            print(f'Sold {quantity} units of {item}. Remaining stock: {self.stock[item]}')
               
            if self.stock[item] == 0:
                del self.stock[item] 
                print(f'Updated stock {self.stock}')
        else: 
            print(f"Not enough stock to sell {quantity} units of {item}.")
            


    def add_stock(self, item_name, item):
        self.stock[item_name] = item
        print(self.stock)
my_product = Product("Fruits", 5)
my_product.add_stock("orange", 3)
my_product.add_stock("grapes", 6)
my_product.sell_units("orange", 1)
my_product.sell_units("orange", 1)
my_product.sell_units("orange", 1)
my_product.sell_units("grapes", 1)

import time
class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def conver_to_sec(self):
        
        while self.hours > 0 or self.minutes > 0 or self.seconds > 0:
            print(f'{self.hours: 02}:{self.minutes: 02}:{self.seconds: 02}', end="\r")
            time.sleep(1)
            self.decrement()

        print("The timer has finished")   
    
    def decrement(self):
        if self.hours > 0:
            self.hours -= 1
        elif self.minutes > 0:
            self.minutes -= 1
        elif self.seconds > 0:
            self.seconds -= 1
             
my_tempo = Timer(0, 0, 10)
my_tempo.conver_to_sec()