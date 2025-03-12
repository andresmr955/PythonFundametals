#List Comprehensions: [expresion for item in iterable if condition]

squaresX2 = [x**2 for x in range(1,11)]
print(f'Los cuadrados de x son => {squaresX2}')

squaresX3 = [x**3 for x in range(1,11)]
print(f'Los cuadrados de x son => {squaresX3}')


celcius = [0, 10, 20, 30, 40]
farenheit =[(temp * 9/5) + 32 for temp in celcius]
print(f'Temperature in F: {farenheit}')

#Find the pairs numbers
numbersx = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print(f'This is my list of numbers: {numbersx}')
paresx = [numberToIterate for numberToIterate in numbersx if numberToIterate % 2 == 0]
print(f'Estos son los pares de la lista numbersx: => {paresx}')

#We can work with a matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(f'Este es el transposed=> {transposed}')

#other expample with a matrix (2x3)

matrixb = [[1,2,3], [4,5,6]]
print(f'This is the matrixb: => {matrixb}')
transposedb = [[rowb[i] for rowb in matrixb] for i in range(len(matrixb[0]))]
print(f'This is the transposedb: => {transposedb}')

matrixa = [[5,8,9,4],[4,5,6,7],[8,5,1,5],[1,2],[1,2,2]]
print(matrixa)
transposeda = [[rowa[i] for rowa in matrixa] for i in range(len(matrixa[0]))]
print(transposeda)