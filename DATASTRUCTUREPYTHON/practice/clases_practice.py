class Persona:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def greet(self):
        print(f'Hello, I am {self.name}')

person = Persona("Andres", 26)
person.greet()

