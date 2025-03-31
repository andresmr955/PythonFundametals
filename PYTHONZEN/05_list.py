'''
numbers = []

for element in range(1, 11):
    numbers.append(element)

print(numbers)

## One line 

numbers = [element for element in range(1,11)]
print(numbers)

numbersx = []

## *2

for element in range(1, 11):
    numbersx.append(element * 2)

print(numbersx)

## One line *2

numbers = [element * 2 for element in range(1,11)]
print(numbers)

'''

numbers = []

for element in range(1, 11):
    if element % 2 == 0:
        numbers.append(element * 2)
    
print(numbers)


numbers = [element * 2 for element in range(1, 11) if element % 2 == 0 ]
print(numbers)
