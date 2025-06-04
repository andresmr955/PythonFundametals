class Employee:
    def __init__(self, name, *args, **kwargs) -> None:
        self.name = name
        self.skills = args
        self.kwargs = kwargs

    def show_employee(self):
        print(f'Employee: {self.name}')
        print(f'Skills: {self.skills}')
        print(f'Details: {self.kwargs}')

employee = Employee('Carlos', 'Python', 'Java', 'C++', age=30, city='Bogota', country='Colombia') 
employee.show_employee()