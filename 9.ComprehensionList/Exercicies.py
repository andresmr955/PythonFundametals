#Doubling of Numbers
#Given a list of numbers [1, 2, 3, 4, 5], create a new list containing twice each 
# number using a List Comprehension.

#Datos de entrada
listOne = [ 1, 2, 3, 4, 5]
#Datos de salida listCreated = [1, 1, 2, 2, 3, 3, 4, 5, 5]

#METHOD TO RESOLVE THE ISSUE 
#List Comprehensions: [expresion for item in iterable if condition]
newList = [ item for item in listOne for _ in range(4)]
print(newList)

#Filtrar y Transformar en un Solo Paso
#Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y 
# quieres obtener una nueva lista 
#con las palabras que tengan más de 3 letras y estén en mayúsculas.


#Datos de entrada
excerciseTwo = ["sol", "mar", "montana", "rio", "estrella"]

#METHOD TO RESOLVE THE ISSUE 
#List Comprehensions: [expresion for item in iterable if condition]
excerciseTwoSolution = [ item.upper() for item in excerciseTwo if len(item) > 3]


print(f'This is the solution: => {excerciseTwoSolution}')
#Datos de salida excerciseTwo = ["MONTANA", "ESTRELLA"]

numbers_given = [1,2,3,4,5,6,7,8,9,10]
double_numbers = [item * 2 for item in numbers_given]
print("Solution 1 => ", double_numbers)
        