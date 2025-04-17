from node import Node

class SingleLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            
            current.next = node
            self.size += 1

    def size(self):
        return str(self.size)
    
    def iter(self):

        current = self.tail
        while current:
            value = current.data
            current = current.next 
            yield value

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            
            previous = current
            current = current.next

    def print_list(self):
        current = self.tail
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(elements), type(elements))       

myangielis = SingleLinkedList()

myangielis.append("M")
myangielis.append("E")
myangielis.append("L")
myangielis.append("O")
myangielis.append("D")
myangielis.append("I")
myangielis.append("E")
myangielis.print_list()

print(myangielis.delete("D"))
myangielis.print_list()