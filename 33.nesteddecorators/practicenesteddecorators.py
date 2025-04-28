def validator(func):
    def wrapper(number):
        if number < 0:
            return "Error: Number must be positive"
        return func(number)
    return wrapper

def multiply_by_ten(func):
    def wrapper(number):
        result = func(number)
        if isinstance(result, (int, float)):
            return result * 10
        return result 
    return wrapper

@multiply_by_ten
@validator
def get_number(number):
    return number

print(get_number(10))
print(get_number(-10))