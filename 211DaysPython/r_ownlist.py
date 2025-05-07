
class MyList:
    def __init__(self, initial_data= None):
        # Tu código aquí 👇
        self.data = initial_data if initial_data else []
        self.length = 0
    
    def __getitem__(self, index):
        return self.data[index]
    
my_o_List = MyList()

my_o_List.append(1)
my_o_List.append(2)
my_o_List.append(3)
my_o_List.append(4)
my_o_List.append(5)

print([i for i in my_o_List])
#my_o_List.append(3)


#new_list = my_o_List.map(lambda x: x * 2)
#print(new_list)

print(my_o_List.filter(lambda x: x > 2))
print(my_o_List.join(character="x"))