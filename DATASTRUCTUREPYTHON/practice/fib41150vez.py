from functools import reduce
num = 8

def fibo_func(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:

        return fibo_func(num - 1) + fibo_func(num - 2)


print(fibo_func(num))

def fibo_dos(num):

    a, b = 0, 1

    for _ in range(num):
        a, b = b, a + b
    
    return a

print(fibo_dos(num))

def fibonacci(num):

    return reduce(lambda acc, _:(acc[1], acc[0] + acc[1]), range(num), (0,1))[0]

print(fibonacci(8))