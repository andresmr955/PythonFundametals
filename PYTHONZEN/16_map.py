numbers = [1, 2, 3, 4, 5]

numbers_2 = []

for i in numbers:
    numbers_2.append(i * 2)
print(numbers)
print(numbers_2)


numbers_3 = list(map(lambda i: i * 2, numbers))
print(numbers_3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

sum_lambda_map = list(map(lambda x, y : x + y,  numbers_1, numbers_2))
print(sum_lambda_map)


