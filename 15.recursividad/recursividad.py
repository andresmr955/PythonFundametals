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
    
## method .isdigit()
# 


numero_usuario_input = input("Give an int positive number: => ")

def suma_de_digitos(numero_usuario):
    if not numero_usuario.isdigit():
        print("Please enter a int positive number: ")
        return
    elif numero_usuario == 0:
        print("Please give a number different to zero")
    else:
        suma = 0
        for i in str(numero_usuario):
            suma += int(i)
        print(suma)
    
suma_de_digitos(numero_usuario_input)

## Calcular la sumatoria de numeros naturales
## Ejemplo 4 = 4 + 3 + 2 + 1
##


def cal_sumatoria(x):
    if x == 0:
        return 0
    else: 
        return x + cal_sumatoria(x - 1)
    
print(cal_sumatoria(4))
4
3
2
1
0

## factorial de un numero 

def factEjerc(x):
    if x == 0:
        return 1
    else: 
        return x * factEjerc(x - 1)

print(factEjerc(5))

5 * 4
4 * 3
3 * 2
2 * 1
1 * 0
