from node import Node

class SingleLinkedList:
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, data):
        add_new = Node(data)
        
        self.tail.next = add_new
        self.tail = add_new
        self.length += 1

        return self.head

    def print_list(self):

        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

mysinlelinkedlits = SingleLinkedList(1)
mysinlelinkedlits.append(2)
mysinlelinkedlits.append(3)
mysinlelinkedlits.append(4)
mysinlelinkedlits.append(5)
mysinlelinkedlits.append(6)
mysinlelinkedlits.append(7)

mysinlelinkedlits.print_list()
