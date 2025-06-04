'''
class Person():
    def __init__(self, name,  age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"my student id is {self.student_id}")
        

student = Student("Ana", 20, "S123")
student.greet()
'''

#### Super level by level

class LivingBeen:
    def __init__(self, name):
        self.name = name
    
class Person(LivingBeen):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        print(f"Helo, everybody! My name is {self.name}")

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def greet_student(self):
        super().greet()
        print(f"My id is {self.id}")
        
student = Student("Andres", 26, 6454)
student.greet()