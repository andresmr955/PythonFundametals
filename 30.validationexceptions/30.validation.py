def divide(a:int, b:int) -> float:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Error both parameter should be integers or floats")
    if b == 0:
       raise ValueError("Error: The divisor can not be zero")
    return a/b


try:
    res_1 = divide(10,"2")

except TypeError as e:
    print(f'Error: {e}')

try: 
    res_2 = divide(10,0)
    print(res_2)
except ValueError as e:
    print(f'Error: {e}')

try: 
    res_3 = divide(10,2)
    print(res_3)
except TypeError as e:
    print(f"Error: {e}")
    