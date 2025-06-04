class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name 
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Hi, my name is {self.name}, I am {self.age}"
    

employe1 = Employee("Carlos", 30, 3500.0)

print(employe1.introduce())

isinstance()