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
