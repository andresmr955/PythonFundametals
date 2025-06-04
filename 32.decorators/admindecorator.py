def admin_access(func):
    def wrapper(initiator, target):
        if initiator.get('rol') == 'admin':
            return func(target)
        else:
            print(f'access denied, just the admins can access')
    return wrapper

@admin_access
def delete_employee(employee):
    print(f'Employee {employee.get('name')} has been deleted')

employees = { "name": "Bob Johnson", "rol": "employee"}
admins = {"name":"Alice Smith","rol": "admin"}

delete_employee(admins, employees)
delete_employee(employees, admins)