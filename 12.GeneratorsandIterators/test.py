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