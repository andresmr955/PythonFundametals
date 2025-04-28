from datetime import datetime
import time

employees = { "name": "Bob Johnson", "role": "employee", "actions" : ["clock in", "clock out", "work", "delete employees"]}
admin = {"name":"Alice Smith","role": "admin", "actions" : ["clock in", "clock out", "work", "delete employees"]}

print( admin["actions"][0])
def check_access(required_arg):
    def decorator(func):
        def wrapper(employee, action):
            if employee["role"] != required_arg:
                return f'Only {required_arg} can access to this feature'
            return func(employee, action)
        return wrapper
    return decorator
    
def log_employee_action(func):
    def wrapper(employee, action):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        result = func(employee, action)

        with open('./33.nesteddecorators/loggings.txt', mode="a") as file:
            file.write(f'{timestamp} - {result}\n')
        return result    
    return wrapper


@log_employee_action
@check_access('admin')
def action_employee(employee, action):
    return f"action {action} performed by {employee['name']}"

result = action_employee(admin, admin["actions"][0])
result2 = action_employee(employees, employees["actions"][3])
print(result)
print(result2)
result = action_employee(admin, admin["actions"][3])
print(result)
