class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        #this is a protected attribute
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Salary must be a non-negative number")
        self._salary = value

    @salary.deleter
    def salary(self):
        print(f"Deleting salary... of {self.name}")
        del self._salary

#Creating an instance of Employee
employee = Employee("John Doe", 50000)
print(employee.salary)  # Output: 50000

#modifying the salary in a controlled way
employee.salary = 60000
print(employee.salary)  # Output: 60000

# Attempting to set an invalid salary
try:
    employee.salary = -1000  # Raises ValueError   
except ValueError as e:
    print(e)

#deleting the salary attribute
del employee.salary  # Output: Deleting salary... of John Doe
# Attempting to access the deleted salary attribute will raise an AttributeError