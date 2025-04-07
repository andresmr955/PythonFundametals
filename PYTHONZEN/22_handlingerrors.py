print("Hola")

#print(0/0)

suma = lambda x, y: x + y 

assert suma(2,2) == 4

print("End")
age = 18
if age < 18:
    raise Exception("Only older than 18")