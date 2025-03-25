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