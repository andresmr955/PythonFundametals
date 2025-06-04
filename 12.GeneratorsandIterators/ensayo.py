comienza = 0
nNumeros = 5
contador = 0  # Para contar cuántos pares llevamos

while contador < nNumeros:
    if comienza % 2 == 0:
        print(comienza)  # Imprime el número par
        contador += 1  # Aumentamos el contador
    comienza += 1  # Pasamos al siguiente número

### GENERATOR

def generadorPares(n):
    numberLoop = 0
    count = 0
    while count < n:
        if numberLoop % 2 == 0:
            yield numberLoop
        numberLoop += 1
        count += 1
        

gen = generadorPares(10)
for num in gen:
    print("This is the generador ", num)

#############################################################
    
def fibonacci(n):
    x,y = 0,1 
    countx = 0
    while countx < n:
        yield x
        x, y = y, x + y
        countx += 1  
genx = fibonacci(1000)
for numx in genx:
    print(f'This is the num binoacci => {numx}')