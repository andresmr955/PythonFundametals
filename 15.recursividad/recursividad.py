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