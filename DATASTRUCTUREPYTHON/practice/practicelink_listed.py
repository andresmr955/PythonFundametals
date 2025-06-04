from node import Node

class MySingleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, data):
        '''
        Recibe un valor y lo convierte en la siguiente cola
        El null nos da la oportunidad de agregar un nuevo nodo
        '''
        new_node_ap = Node(data)

        if self.head is None:
            self.head = new_node_ap
            self.tail = new_node_ap
        else:
            self.tail.next = new_node_ap
            self.tail = new_node_ap

        self.length += 1

        
mylinkedlist = MySingleLinkedList(10)
print(mylinkedlist.head.data)
print(mylinkedlist.length)
mylinkedlist.append(20)
print(mylinkedlist.tail.data)