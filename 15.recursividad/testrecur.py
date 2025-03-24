a = int(input("Primer numero"))
b = int(input("Segundo  numero"))

def potencia_numero(x,y):
    if y == 0:
        return 1
    else:
        return x * potencia_numero(x, y - 1) 
    
    
print(potencia_numero(a,b)) 