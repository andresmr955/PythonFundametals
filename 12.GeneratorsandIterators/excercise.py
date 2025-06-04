'''
tareas = ["Lavar platos", "Sacar la basura", "Comprar comida", "Leer un libro"]

iterator_list = iter(tareas)

while True:
    try: 
        print(next(iterator_list))
        user_enter = input("Click Enter to continue with the next work")
    except StopIteration:
        print("Iterator exhausted")
        break
'''


'''
productos = [
    {"Producto" : "Manzana", "cantidad": 50}, 
    {"Producto" : "Pera", "cantidad": 30}, 
    {"Producto" : "Cocombre", "cantidad": 20}, 
    {"Producto" : "Courge", "cantidad": 10}, 
]

recorrer_productos = iter(productos)


for i in recorrer_productos:
    if i["cantidad"] >= 30:
        print(f'{i["Producto"]} esta bien surtido, hay {i["cantidad"]}')
    else:
        print(f'{i["Producto"]} Esta bajo el surtido, hay {i["cantidad"]}')    
  
'''
'''


def primo(x):
    while True:
        if x <= 1:
            yield f"{x} no es primo"
        elif x == 2 or x == 3:
            yield f"{x} es primo"
        elif x % 2 == 0 or x % 3 == 0:
            yield f'{x} no es primo'
        else:
            es_primo = True
            for i in range(5, int(x ** 0.5)+ 1, 2):
                if x % i == 0:
                    yield f"{x} no es primo"
                    es_primo = False
                    break
            if es_primo:
                yield f"{x} es primo"
        x += 1   

for i in primo(1):
    print(i)
'''
''''

def numbers_fibo(n):
    x, y = 0 , 1
    
    while x <= n: 
        yield x 
        x, y = y, x +y

for i in numbers_fibo(20):
    print(i)

test = numbers_fibo(200)
print(list(test))




'''

'''
class CuentaRegresiva:
    def __init__(self, inicio):
        self.inicio = inicio
        self.numero = inicio


    def __iter__(self):
        return self 
        
    def __next__(self):
       if self.numero <= 0:
           raise StopIteration
       else:
           self.numero -= 1
           return self.numero + 1
       

cuenta = CuentaRegresiva(10)

for i in cuenta:
    print(i)
'''



class Pares:
    def __init__(self, numero):
        # Asegurar que el número sea par
        self.numero = numero if numero % 2 == 0 else numero + 1  

    def __iter__(self):
        return self

    def __next__(self):
        resultado = self.numero  # Guardar el número actual para retornarlo
        self.numero += 2  # Avanzar al siguiente número par
        return resultado  # Retornar el número par actual

# Crear una instancia del iterador de números pares
pares = Pares(4)  

# Obtener los primeros 5 números pares
for _ in range(5):
    print(next(pares))



class IteradorPalabras:
    def __init__(self, phrase):
        self.pharse = phrase.split(' ') 

    def __iter__(self):
        return self
    
    def __next__(self):
        
        resultado = self.pharse
        return resultado 
         

oracion = IteradorPalabras("Aprender a programar es divertido")

for palabra in oracion:
    print(palabra)         


    oracion = "Aprender a programar es divertido"

def iteration_function(x):
    words = x.split(' ')

    myiterador = iter(words)

    for palabra in words:
        print(palabra)

    return myiterador

iteration_function(oracion)

class IteradorPalabras:
    def __init__(self, oracion):
        self.palabras = oracion.split(' ')
        self.indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice >= len(self.palabras):
            raise StopIteration
        palabra = self.palabras[self.indice]
        self.indice += 1

        return palabra
    
oracion = IteradorPalabras("Aprender a programar es divertido")

# Iterar con un bucle for
for palabra in oracion:
    print(palabra)


class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero 
        self.inicio = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.inicio > 10:
            raise StopIteration
        resultado = f'{self.numero} x {self.inicio} = {self.numero *  self.inicio} '
        self.inicio += 1

        return resultado

tabla = TablaMultiplicar(8)

for resultado in tabla:
    print(resultado)

