class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node_one = Node("A", None)
node_two = Node("B", node_one)
node_three = Node("C", node_two)
node_four = Node("D", node_three)
node_five = Node("E", node_four)
node_six = Node("F", node_five)
node_seven = Node("G", node_six)
node_eight = Node("H", node_seven)
node_nine = Node("I", node_eight)
node_ten = Node("J", node_nine)
print(node_one.data)
print(node_two.data)
print(node_three.data)
print(node_four.data)
print(node_five.data)
print(node_six.data)
print(node_seven.data)
print(node_eight.data)
print(node_nine.data)
print(node_ten.data)

head = node_ten

while head != None:
    print(head.data)
    head = head.next



while head != None:
    print(f'This is data head {head.data} and here is the next {head.next}')
    head = head.next




def func_add_node(head_parameter, data_parameter):
    if head_parameter == None:
        return Node(data_parameter, head_parameter)
    
    actual = head_parameter

    while actual.next != None:
        actual = actual.next

    actual.next = Node(data_parameter, None)

    return head_parameter

# We create the list with nodes
head = None
for i in range(0, 100,  2):
    head = Node(i, head)

#Show the nodes before add the new node
current = head
while current != None:
    print(current.data)
    current = current.next

print("Lista recorrida completamente")
    


#We add a new node with 200 as a value 
head = func_add_node(head, 200)

# We show the nodes with 200 added
current = head
while current != None:
    print(current.data)
    current = current.next