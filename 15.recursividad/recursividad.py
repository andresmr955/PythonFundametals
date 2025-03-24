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
    



def fibowhile(j):
    k, l = 0, 1
    contador = 0
    while contador < j:
        yield  k
        k, l = l, k + l  
        contador +=1

for i in fibowhile(8):
    print(i)
    

    