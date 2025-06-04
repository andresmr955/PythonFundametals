addition = lambda a,b: a + b 
subtraction = lambda a, b: a - b
multiply = lambda a , b: a * b

##The only expression it can not work with lambda is conditional and raise
def divide(a, b):
    if b == 0:
        raise ValueError("It is not possible to divide by 0")
    else: 
        return a / b     
