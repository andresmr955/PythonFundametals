from array_02 import Array ##Change the name when you want to deploy

from grid_03 import Grid

class Cube():
    def __init__(self, rows, columns, deep, fill_value=None):
        
        self.data = Grid(rows, columns)
        for row in range(len(self.data)):
            for column in range(len(self.data[0])):
                self.data[row][column] = Array(deep, fill_value)
    
    def __str__(self):
        result = " [\n"
        for row in self.data:
            result += "  ["
            for column in row:
                result += str(column) + ", "
            result = result.strip(", ")
            result += "],\n"
        result += "],"
        return result

cube = Cube(3, 3, 3, "x")
print(cube)