from array_02 import Array

class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
    
    def get_height(self):
        return len(self.data)
    
    def get_weight(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_weight()):
                result += str(self.data[row][col]) + " "

            result += "\n"
        return str(result)
    

matrix = Grid(3,3)
#print(matrix)

for row in range(matrix.get_height()):
    for column in range(matrix.get_weight()):
        matrix[row][column] = row * column

print(matrix)


print("height:", matrix.get_height())
print("weight:", matrix.get_weight())
print("Item 1 complete:", matrix.__getitem__(1))
print("Item 1, element 0:", matrix.__getitem__(1)[0])
print("Item 1, element 1:", matrix.__getitem__(1)[1])
print("Representation in string:", matrix.__str__())
