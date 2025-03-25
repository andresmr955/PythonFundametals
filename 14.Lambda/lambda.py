add = lambda a, b: a + b
subtraction = lambda a, b: a - b
multiply = lambda a , b: a * b

##square number
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers ))
print(squared_numbers)