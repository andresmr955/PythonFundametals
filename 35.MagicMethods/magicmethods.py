class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Person: {self.name}, {self.age} years old'

person = Person("Andres", 26)
print(person)

class Toy:
    def __init__(self, name):
        self.name = name

    def __add__(self, other_toy):
        return Toy(self.name + " and " + other_toy.name)

# Create two toys
toy1 = Toy("Car")
toy2 = Toy("Airplane")

# Use the magic method __add__ to "add" the toys
toy3 = toy1 + toy2

print(toy3.name)  # Output: Car and Airplane

class Toy:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __add__(self, other_toy):
        # Corrected: Now we pass both arguments, name and model, to the constructor
        return Toy(self.name + " and " + other_toy.name, self.model + other_toy.model)

# Create two toys
toy1 = Toy("Car", 2000)
toy2 = Toy("Airplane", 1989)

# Use the magic method __add__ to "add" the toys
toy3 = toy1 + toy2

print(toy3.name)
print(toy3.model)
