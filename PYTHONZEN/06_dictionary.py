dict = {}

for i in range(1,5):
        dict[i] = i * 2
print(dict) 

dict_list_num = [{i: i*2 for i in range(1,5)}]
print(dict_list_num)


dict = {}
abcd = ["a", "b", "c", "d"]
for i in range (1, 5):
        dict[i] = abcd[ i - 1]
print(f'This is my dict  {dict}')

dictx = {i : abcd [i - 1] for i in range(1,5) }
print(f'This is my comprehension list {dictx}')

import random 

countries = ['col', 'mex', 'bol', 'per']
population = {}
for country in countries:
        population[country] = random.randint(1,100)
#Create values to the keys
print(population)


population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

exercise_ages = {names[i]: ages[i] for i in range(len(names))}
print(exercise_ages)

##Tenemos zip una funcion que hace una union entre una lista y otra
print(zip(names, ages))

print(list(zip(names, ages)))

new_dict = {name:age for (name, age) in zip(names, ages)}
#print(new_dict)