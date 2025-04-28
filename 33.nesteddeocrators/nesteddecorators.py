# Decorator that checks if an employee has a specified role
def check_access(required_role):
        # Step 1: This function receives the "required_role" parameter, which is the role needed.
    def decorator(func):
          # Step 2: The decorator takes the function you want to decorate, "func".
        def wrapper(employee):
            # Step 3: The wrapper function checks if the employee's role matches the required role.
            #We check if the rol's employee coincides  with a required rol
            if employee.get('role') == required_role:
                # Calls the original function if the role is correct.
                return func(employee)
            else:
                print(f'Access denied. Just {required_role} can do this action')
               #The decorator returns the wrapper function.
        return wrapper
        ## The "check_access" function returns the decorator.
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registering to the employees {employee['name']}')
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'The employee {employee['name']}, has been deleted')



employees = { "name": "Bob Johnson", "role": "employee"}
admins = {"name":"Alice Smith","role": "admin"}

delete_employee(admins)