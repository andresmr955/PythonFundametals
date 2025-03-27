numbers = [1, 2, 3, 4, 5]

'''
This is not a good practice
squares = []

for number in numbers:
    square = number ** 2
    squares.append(square)

'''

squares = [number **2 for number in numbers]

print(squares)
