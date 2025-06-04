class Vector:
    def __init__(self, x , y):
        self.x = x 
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)
    def __repr__(self):
        return f'Vector: (X {self.x}, Y {self.y})'
    
vector1 = Vector(1,2)
vector2 = Vector(2,1)
vector3 = vector1 + vector2
print(vector3)



