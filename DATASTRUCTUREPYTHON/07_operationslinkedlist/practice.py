from node import Node

from node import Node

class SingleLinkedList():
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
    
    def print_list(self):
        current = self.tail
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("--> ".join(elements))    

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current.next:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data 

            previous = current
            current = current.next
        
    def search(self, data):
        
        for node in self.iter():
            if node == data:
                print(f'we found {data}')
                return
            else:
                print("We could not find it")

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0


    def delete_any(self, index):
        
        if index <= 0 or self.tail is None:
            print("Index out of bounds or empty list.")
            return

        if index == 1:
            removed_item = self.tail.data
            self.tail = self.tail.next
            print(f'Item removed: {removed_item}')
            return

        probe = self.tail
        current_index = 1

        while probe.next and current_index < index - 1:
            probe = probe.next
            current_index += 1

        if probe.next is None:
            print("Index out of bounds.")
            return

        removed_item = probe.next.data
        probe.next = probe.next.next
        print(f'Item removed: {removed_item}')


mylinkedlist = SingleLinkedList()
mylinkedlist.append("A")
mylinkedlist.append("B")
mylinkedlist.append("C")
mylinkedlist.append("D")

mylinkedlist.print_list()
mylinkedlist.delete_end(1)
