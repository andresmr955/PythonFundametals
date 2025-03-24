def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n-1)

print(factorial(30))

def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else: 
        return  fibonacci(a-1) + fibonacci(a-2)

number = 4
print(fibonacci(number))
    
