import random
from functools import reduce

class Array: 
    def __init__(self, capacity, fill_value=None):
        self.capacity  = capacity
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        if self.items:
            return f'Array ({len(self.items)} items, first: {repr(self.items[0])}, last: {repr(self.items[-1])})'
        else:
            return f'Array ({len(self.items)} items, Empty)'
        
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item
        return self.items
    
    def replace_elements(self, lower, upper):
        self.items= [ random.randint(lower, upper) for i in range(len(self.items))]      
        return self.items
    
    def sum_all_elements(self):
        return reduce(lambda start, final: start + final, self.items)

my_array = Array(10, "A")
print(my_array)
print(my_array.__len__())
print(my_array.__repr__())
print(my_array.__getitem__(5))
print(my_array.__setitem__(-1, "M"))


##Crear un metodo que remplaze el valor de sus elementos: Ya sea numeros aleatorios o consecutivos
##Sumar el valor de todos los elementos que hay en el array: si son strings, caracters o numeros Pista recorrer el array y saber que hay en cada uno de sus elementos y sumarlso de forma iterativa usando su metodo iterador
print(my_array.sum_all_elements())

print(my_array.replace_elements(0, 100))
print(my_array.sum_all_elements())
