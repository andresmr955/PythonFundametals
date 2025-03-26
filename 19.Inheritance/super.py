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