#Ejercicio 1: Crear un set y eliminar duplicados

numeros = [1, 2, 3, 4, 4, 5, 6, 2, 7, 8, 8, 9, 10]

set_x = set(numeros)
print(f'This is the set function: => {set_x}')
#Ejercicio 2: Unión e intersección de sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_x = set1.union(set2)
print(f'This is the union: => {union_x}')

intersection_x = set1.intersection(set2)
print(f'This is the intersection: => {intersection_x}')
## Ejercicio 3: Diferencia entre sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
##Which ones are in the first group that are not in the segund group
difference_x = set1.difference(set2)
print(f'This is the difference: => {difference_x}')

#Ejercicio 4: Verificar si un elemento está en un set

'''
numeros = {3, 6, 9, 12, 15}
numero_usuario = int(input('Íngresa un numero para verificar si esta en nuestro conjunto: => '))

if numero_usuario in numeros:
    print(f'This {numero_usuario} number is in the set')
else:
    print(f'This {numero_usuario} number is not in the set')
'''

#Ejercicio 5: Eliminar elementos de un set

colores = {"rojo", "azul", "verde", "amarillo"}
print(colores)
eliminar = "azul"
result = colores.discard(eliminar)

#colores.remove(eliminar)
print(f'This is using .remove()  and .discard() and the result is {colores}')

#Ejercicio 6: Encontrar diferencias simétricas
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = set1.symmetric_difference(set2)
print(f'This is using .symmetric_difference() and the result is {result}')

#Ejercicio 7: Convertir un set en una lista ordenada

numeros = {8, 3, 1, 6, 2, 5}
###order a dictionary
solution = sorted(numeros)
print(f'Here we are transforming a set in an order list {solution}')