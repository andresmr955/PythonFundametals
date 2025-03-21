#Divide and conquer
#Sirven para guardar porciones de codigo que tienen una tarea especifica

def greet(name ):
    print(f' Hola {name} ')

greet("Andres")

# we can add more parameters


def greetx(name, last_name=" No tiene apellido"):
    print(f' Hola {name} {last_name} ')

greetx("Andres")
greetx("Andres", "marquez")


#Changing postion 

def greety(name, last_name=" No tiene apellido"):
    print(f' Hola {name} {last_name} ')

greety("carla")
greety(last_name="carla", name="platzi")

## we can not positional argument follows keyword argument

##greety(last_name="carla", name)


def whole_operation(customer_choice, x, y):
    suma = "suma"
    resta = "resta" 
    multiplicacion = "multiplicacion"
    division = "division"
    if customer_choice == suma:
        suma = add(x,y)
        print(suma) 

    elif customer_choice == resta:

        resta = subs(x,y)
        print(resta)

    elif customer_choice == division:

        division = div(x,y)
        print(division)
    
    elif customer_choice == multiplicacion:

        multiplicacion = multi(x,y)
        print(multiplicacion)

    
def add(a, b):
    return a + b
def subs(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    return a / b

customer_choice = input("Escirbe tu operacion: => ")
x = int(input("Escirbe tu primer numero a operar: => "))
y = int(input("Escirbe tu segundo numero a operar: => "))

whole_operation(customer_choice, x, y)