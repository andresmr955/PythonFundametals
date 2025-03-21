

class EjemploIterator:
        def __init__(self, numero):
            self.inicio = 0
            self.numero = numero
        def __iter__(self):
             return self
        
        def __next__(self):
            if self.inicio <= 10: 
                resultado = f'{self.numero} x {self.inicio} equal to {self.numero * self.inicio}'
                self.inicio += 1
                return resultado  
            else:     
               raise StopIteration  
EjemploIterator(7)

for i in EjemploIterator(7):
     print(i)




def print_triangle(size,character):
    contador = 1

    while contador <= size:
        espacios = " " * (size - contador) 

        output = espacios + character * (contador * 2 - 1 ) + "\n"
        
        if contador != size - 1:
            output += "\n"
        
    
        contador+= 1
        return output
        
print_triangle(3, "x")
