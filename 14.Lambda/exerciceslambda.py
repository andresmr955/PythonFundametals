numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtering_numbers_impairs = filter(lambda a : a % 2 != 0, numbers)

squared_odd = list(map(lambda b: b ** 2, filtering_numbers_impairs))


print(squared_odd)