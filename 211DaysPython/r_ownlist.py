
class MyList:
    def __init__(self, initial_data= None):
        # Tu código aquí 👇
        self.data = initial_data if initial_data else {}
        self.length = len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        return f"My list: {self.data}"
    
    def append(self, item):
        # Tu código aquí 👇
        self.data[self.length] = item
        self.length += 1
    
        
    def map(self, func):
        mapped_data = {k: func(v) for k, v in self.data.items()}
        return MyList(mapped_data)
    
    
    def filter(self, func):
        new_filter = {}
        new_key = 0
        
        for _, value in self.data.items():
            if func(value)
                new_filter[new_key] = value
                new_key += 1

        return MyList(new_filter)

    def join(self, character=","):
        result = ""
        for i in range(self.length): 
           result += str(self.data[i])
           if i < self.length - 1:
               result += character
        return result

    def pop(self):

        if self.length == 0:
            return None

        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item 
            

    def shift(self):
        new_data = {}
        first_item = self.data[0]
        for i in range(1, self.length):
            
            new_data[i - 1] = self.data[i]

        self.data = new_data
        self.length -= 1
        return first_item

my_o_List = MyList()

my_o_List.append(1)
my_o_List.append(2)
my_o_List.append(3)
my_o_List.append(4)
my_o_List.append(5)

# print([i for i in my_o_List])
#my_o_List.append(3)


#new_list = my_o_List.map(lambda x: x * 2)
#print(new_list)


print(my_o_List.data)
print(f'{my_o_List.filter(lambda x: x if x > 2 else None)}')
print(my_o_List.join(character="x"))
print(my_o_List.pop())
print(my_o_List.data)

print(my_o_List.shift())
print(my_o_List.data)
