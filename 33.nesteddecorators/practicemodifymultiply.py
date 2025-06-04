def multiply_by_ten(func):
    def wrapper(number):
        result = func(number)
        return result * 10
    return wrapper

@multiply_by_ten
def get_number(number):
    return number

print(get_number(5))