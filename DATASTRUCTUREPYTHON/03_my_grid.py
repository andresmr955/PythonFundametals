from array_02 import Array
import random

class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def __len__(self):
        return len(self.data)  # Devuelve la longitud de la lista principal (número de filas)

    def get_height(self):
         return len(self.data)

    def get_width(self):
        return len(self.data[0]) 
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __iter__(self):
        for row in self.data:
            yield row

    def fill_random(self, lower, upper):
        result = 0
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                self.data[row][column] = random.randint(lower, upper) 

        return result    
    
    def __str__(self):
        result = ""
        for row in range(len(self.data)):
            for column in range(len(self.data[0])):
                result += str(self.data[row][column]) + " "  
            
            result += "\n"

        return result
    

matrix = Grid(3,3)


matrix = Grid(3, 3)
matrix.fill_random(0, 100)

#print(matrix)