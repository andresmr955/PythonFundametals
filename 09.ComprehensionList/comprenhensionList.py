#List Comprehensions: [expresion for item in iterable if condition]

squaresX2 = [x**2 for x in range(1,11)]
print(f'Los squares de x son => {squaresX2}')

squaresX3 = [x**3 for x in range(1,11)]
print(f'Los squares de x son => {squaresX3}')


celsius_var = [0, 10, 20, 30, 40]
fahrenheit =[(temp * 9/5) + 32 for temp in celsius_var]
print(f'Temperature in F: {fahrenheit}')

#Find the pairs numbers with a conditional, the order is first for and after condition
numbers_x = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print(f'This is my list of numbers: {numbers_x}')
paresx = [numberToIterate for numberToIterate in numbers_x if numberToIterate % 2 == 0]
print(f'These are the pairs in the list of numbers_x: => {paresx}')

#We can work with a matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(f'This is the transposed => {transposed}')

#other example with a matrix (2x3)

matrix_b = [[1,2,3], [4,5,6]]
print(f'This is the matrix_b: => {matrix_b}')
transposed_b = [[row_b[i] for row_b in matrix_b] for i in range(len(matrix_b[0]))]
print(f'This is the transposed_b: => {transposed_b}')

#This is not valid cause every rectangular matrix has a different length 
#matrix_a = [[5,8,9,4],[4,5,6,7],[8,5,1,5],[1,2],[1,2,2]]
matrix_a = [[5,8,9,4],[4,5,6,7],[8,5,1,5],[1,2,9,7],[9,1,2,2]]

print(matrix_a)

transposed_a = [[row_a[i] for row_a in matrix_a] for i in range(len(matrix_a[0]))]
print(transposed_a)