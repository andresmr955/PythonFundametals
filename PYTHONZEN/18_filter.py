numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(new_numbers)