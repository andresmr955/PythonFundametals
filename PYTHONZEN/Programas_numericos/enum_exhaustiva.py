objective = 25
answer = 0

while answer**2 < objective:
    print(answer)
    answer += 1

if answer**2 == objective:
    print(f'The square root of {objective} is {answer}')
else:
    print(f'{objective} does not have an integer square root')

lista_x = [1, 2, 3, 4, 5]

min = lista_x[4]

for i in lista_x:
    if i < min:
        min = i
        
print(f'The minimum value is {min}')            

# La desventaja es que cuando el numero de posible soluciones es muy grande, el tiempo de computo se vuelve inaceptable.\
# La ventaja es que es un algoritmo sencillo de implementar y entender.
#En problemas donde sea pequeno el numero de soluciones y que necesitamos exactitud 

##cambiando el valor de epsilon podemos mejorar la precicion 

#la diferencia entre una solucion exacta y una aproximada es el maregen de error y tieempo de computo
# usara una solucion aproximada cuando queiro velocidad y no exactitud


## usaria el criterio para parar un algoritmo con epsilon 

##es mas eficiente la busqueda binaria que la lineal porque es mas rapido y se basa en rangos no en verificar todas las soluciones posibles

##debo conocer el bajo el alto 

# no se puede la busqueda binaria solo funciona con una lista ordernada y no con una lista desordenada