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
        

list_words = ["sol", "mar", "montana", "rio", "estrella"]
new_list = [word_x.upper() for word_x in list_words if len(word_x) > 3]
print("Solution 2 => ",new_list)


list_one = ["name", "age", "job_title"]
list_two = ["Juan", 30, "Engineer"]
dictionary_combined = {list_one[i]: list_two[i] for i in range(len(list_one))}
print("Solution 3 => ",dictionary_combined)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_transpuesta = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]


transposed = [[list_inside_list[len_of_list] for list_inside_list in matriz] for len_of_list in range(len(matriz[0])) ]
print(len(matriz[0]))
print("Solution 4 => ",transposed)


personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]


solucion = [ personas[len_dicti]["nombre"] for len_dicti in range(len(personas)) if personas[len_dicti]["edad"] > 30 and personas[len_dicti]["ciudad"] == "Madrid"]


#output = ['This is out output waiting: ', {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},{"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}]
print("Solution 5 => ",solucion)


list_ex_six = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_new_ex_six = [ i * 2 if i % 2 == 0 else i for i in list_ex_six]
print("Solution 5 => ", list_new_ex_six)