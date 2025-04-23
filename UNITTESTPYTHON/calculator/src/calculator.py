# from math import inf
def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
# def divide(a,b):
#     if b != 0:
#         return a / b
#     elif b == 0 and a > 0:
#         return inf
#     elif b == 0 and a < 0:
#         return -inf
#     else:
#         return None
    

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("It is not possible to divide by zero")
    else:
        return a / b    