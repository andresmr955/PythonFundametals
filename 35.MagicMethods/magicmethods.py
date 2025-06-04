class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f'Person: {self.name}, {self.age} years old'

person = Person("Andres", 26)
print(person)

class Toy:
    def __init__(self, name: str):
        self.name = name

    def __add__(self, other_toy) -> str:
        return Toy(self.name + " and " + other_toy.name)

# Create two toys
toy1 = Toy("Car")
toy2 = Toy("Airplane")

# Use the magic method __add__ to "add" the toys
toy3 = toy1 + toy2

print(toy3.name)  # Output: Car and Airplane

class Toy:
    def __init__(self, name: str, model: int):
        self.name = name
        self.model = model
        
    def __add__(self, other_toy) -> str:
        # Corrected: Now we pass both arguments, name and model, to the constructor
        return Toy(self.name + " and " + other_toy.name, self.model + other_toy.model)
    
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age
    
    def __it__(self, other_person) -> bool:
        return self.model < other_person.model

# Create two toys
toy1 = Toy("Car", 2000)
toy2 = Toy("Airplane", 1989)

# Use the magic method __add__ to "add" the toys
toy3 = toy1 + toy2
print(f'__eq__: => {toy1.__eq__(toy2)}')
print(toy3.name)
print(toy3.model)
