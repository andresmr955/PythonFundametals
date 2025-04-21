from practicex import SingleLinkedList

class Array:
    def __init__(self, size, data=None):
        self.size = size
        self.items = []
        for i in range(size):
            self.items.append(data)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def set_item(self, index, new_data):
        if 0 <= index < self.size:
           self.items[index] = new_data
        else:
            raise IndexError("Indice fuera de rango")

    def append_item(self, new_data):
        self.items.append(new_data)
        self.size += 1
        return self.items

myarray = Array(1, "A")
myarray.append_item("B")
myarray.append_item("C") #['A', 'B', 'C']




def add_array_to_link(array_list):
    mylinkedlist = SingleLinkedList()
    for i in array_list:
        mylinkedlist.append(i)

    return mylinkedlist.print_list()

add_array_to_link(myarray.items)