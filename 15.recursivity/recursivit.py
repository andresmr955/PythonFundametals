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
    counter = 0
    while counter < j:
        yield  k
        k, l = l, k + l  
        counter +=1

for i in fibowhile(8):
    print(i)
    
## method .isdigit()
# 


user_input_number = input("Give an int positive number: => ")

def digits_addition(user_number):
    if not user_number.isdigit():
        print("Please enter a int positive number: ")
        return
    elif user_number == 0:
        print("Please give a number different to zero")
    else:
        addition = 0
        for i in str(user_number):
            addition += int(i)
        print(addition)
    
digits_addition(user_input_number)

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
a = int(input("Primer numero"))
b = int(input("Segundo  numero"))

def potencia_numero(x,y):
    if y == 0:
        return 1
    else:
        return x * potencia_numero(x, y - 1) 
    
    
print(potencia_numero(a,b)) 

string_x = "Andres"
print(string_x[-1])

print(len(string_x))


new_string = ""
new_string = string_x[5] + string_x[4] + string_x[3] + string_x[2] + string_x[1] + string_x[0]

print(new_string)

def inverted_string(c):
    len(c)
    new_string = ""
    if len(c) == 0:
        return ""
    else:
        new_string = c[len(c) -1]  + inverted_string(c[:-1])
        return new_string
string_x = "Andres"
print(inverted_string(string_x))

