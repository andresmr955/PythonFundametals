#implementar un decorador llamado log_employee_action que registre cualquier 
# accion realidzada por un empleaado en un archivo de texto

import os

def log_employee_action(func):
    def wrapper(employee_arg, action_arg):
        try:
            result = func(employee_arg, action_arg)
            file_path = './32.decorators/employee_report.txt'

            if not os.path.exists(file_path):
                print('Creating new report...')

            with open(file_path, mode='a') as file:
                file.write(f'{result}\n')
        except Exception as e:
            print(f'An error has occurred: {e}')
    return wrapper

@log_employee_action
def employee_action(employee_arg, action_arg):
    if action_arg == 'View profile':
        result = f'{employee_arg.get('name')} viewed his profile'
    elif action_arg == 'Submit a time-off request':
        result = f'{employee_arg.get('name')} has submit a request'
    elif action_arg == "Clock in/Clock out":
        result = f'{employee_arg.get('name')} is Clock in/Clock out'

    return result 

employee = { "name": "Bob Johnson", "rol": "employee"}
admins = {"name":"Alice Smith","rol": "admin"}

employee_action(employee, 'View profile')
employee_action(employee, 'Submit a time-off request')