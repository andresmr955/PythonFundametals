#A list comprehension is a concise way to create lists in Python. It allows 
# you to generate a new list by applying an expression to each item in an existing 
# iterable (like a list or range) in a single line of code.

#📌 Basic Syntax

new_list = [expression for item in iterable]

#🔹 expression: The operation applied to each item.
#🔹 item: The variable representing each element in the iterable.
#🔹 iterable: The source of elements (e.g., a list, range, or string).

# 📌 Example 1: Generating a List of Squares

squares = [x**2 for x in range(1, 6)]
print(squares)

#🔹 Output: [1, 4, 9, 16, 25]
#✅ The list comprehension squares numbers from 1 to 5.

#📌 Example 2: Filtering with Conditions (if statement)
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

#🔹 Output: [0, 2, 4, 6, 8]
#✅ Only even numbers are included.

#📌 Example 3: Applying a Function Inside List Comprehension

def double(x):
    return x * 2

doubled_numbers = [double(x) for x in range(1, 6)]
print(doubled_numbers)

#🔹 Output: [2, 4, 6, 8, 10]
#✅ Each number is doubled using the function.

#📌 Example 4: Using if-else in List Comprehension
numbers = [x if x % 2 == 0 else 'odd' for x in range(6)]
print(numbers)

#🔹 Output: [0, 'odd', 2, 'odd', 4, 'odd']
# ✅ Replaces odd numbers with "odd".

#📌 Example 5: Nested List Comprehensions (Matrix Transposition)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transposed)

#🔹 Output:


# [[1, 4, 7], 
# [2, 5, 8], 
# [3, 6, 9]]

#✅ This transposes a 3x3 matrix using a nested list comprehension.

#📌 Example 6: Handling Lists of Different Lengths (zip_longest)
#If lists have different lengths, zip_longest() from itertools helps:


#from itertools import zip_longest

matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
transposed = [list(row) for row in zip_longest(*matrix, fillvalue="X")]

print(transposed)
#🔹 Output:

# [[1, 4, 6], 
#  [2, 5, 7], 
#  [3, 'X', 8], 
#  ['X', 'X', 9]]
# ✅ It fills missing values with "X" to prevent errors.

