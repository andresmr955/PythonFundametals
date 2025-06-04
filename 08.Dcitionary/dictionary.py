numbers = {1: "One", 2: "Two", 3:"Three"}
print(numbers[2])
information = {
    "name": "carla", 
    "LastName": "Florida", 
    "height": 1.60,
    "Age":29
}
print(f'This is the completely information: => {information}')


#To delete a key
del information["Age"]
print(f'This is without the key deleted information: => {information}')

claves = information.keys()
print(claves)
valores = information.values()
print(valores)
Pairs = information.items()
print(Pairs)