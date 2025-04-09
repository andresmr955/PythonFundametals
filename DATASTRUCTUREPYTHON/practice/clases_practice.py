class Persona:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def greet(self):
        print(f'Hello, I am {self.name}')

person = Persona("Andres", 26)
person.greet()

class Rectangle():
    def __init__(self, weight, hight):
        self.weight = weight
        self.hight = hight
    
    def calculate_area(self):
        return self.weight * self.hight
    
    def perimeter(self):
        total = 2 * (self.weight + self.hight)
        return total
    
rectangle = Rectangle(20, 10)
print(rectangle.perimeter())
print(rectangle.calculate_area())