
### Exercise 1
sum_numbers = lambda x, y : x + y

print(sum_numbers(4,5))
print(sum_numbers(5,9))
print(sum_numbers(2,7))


### Exercise 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


solution = list(filter(lambda x : x % 2 == 0 , numbers))

print(solution)

#Exercise 3

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x : x ** 2, numbers))
print(squared)

#Exercise 4

words = ["Python", "Lambda", "Ejercicios", "Código", "Fun"]

solution = lambda x: sorted(x, key=len)
print(solution(words))

#Define un diccionario de funciones lambda para realizar diferentes operaciones matemáticas.

operaciones = {
    "add" : lambda x, y: x + y, 
    "substract" : lambda x, y: x - y, 
    "multiply" : lambda x, y: x * y, 
    "divide" : lambda x, y: x / y, 
}

print(operaciones["add"](7,8))