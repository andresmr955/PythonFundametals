# from math import inf
def sum(a, b):

    """ 
    >>> sum(5,7)
    12
    
    
    >>> sum(5,10)
    15
    """
    return a + b

   
def subtract(a, b):
    return a - b

def multiply(a, b):
    """
    >>> multiply(3,3)
    10

    """
    
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

    """

    >>> divide(15,5)
    3.0
    >>> divide(10, 0)
    Traceback (most recent call last): 
    ZeroDivisionError: It is not possible to divide by zero
    """
    if b == 0:
        raise ZeroDivisionError("It is not possible to divide by zero")
    else:
        return a / b  

if __name__ == "__main__":
    import doctest
    doctest.testmod()