numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtering_numbers_impairs = filter(lambda a : a % 2 != 0, numbers)

squared_ = list(map(lambda b: b ** 2, filtering_numbers_impairs))


print(squared_)


names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

names_with_more_five = filter(lambda a: len(a) >= 5 ,names)

upper_names = list(map(lambda b: b.upper(), names_with_more_five))

print(upper_names)

names = {'Nicolas', 'Miguel', 'Juan', 'Nicolas'} 
print(names) 

a = {1,2}
b = {2,3}
print(a - b)