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