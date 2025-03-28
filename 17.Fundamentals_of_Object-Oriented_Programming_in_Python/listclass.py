class Array:
    def __init__(self):
        
        self.data = []

    def get(self, index):
        return self.length[index]

    def append(self, item):
        self.data.append(item)

    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)
my_array = Array()

my_array.append("Andres")
print(len(my_array), my_array)