# We create a class called Array
# Representation of an array per se
class Array:
    # Constructor: define capacity, size, and the value to fill
    def __init__(self, capacity, fill_value=None):
        # We store it in an empty list
        self.items = list()
        # We have the default values in each of the elements of our array according to its capacity
        for i in range(capacity):
            self.items.append(fill_value)
    
    # Private method that will allow us to know its length or size
    def __len__(self):
        return len(self.items)
    
    # Represent it as a string of each of its elements
    def __str__(self):
        return str(self.items)
    
    # Iterator: helps us traverse the structure, assign values, and change them
    # Private method that helps us get the iterator of the elements
    def __iter__(self):
        return iter(self.items)
    
    # Private method: get the element with index as an attribute
    def __getitem__(self, index):
        return self.items[index]
    
    # Method to replace elements
    def __setitem__(self, index, new_item):
        self.items[index] = new_item
