
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# We declare 3 variables

#This node does not have value
node_1 = None
#This node has a value but it has not pointer
node_2 = Node("A", None)
#This node has value and its pointer is node_2
node_3 = Node("B", node_2)

'''
#Here we print the node_2 but it shows its location 
print(f'we print the node_2 but it shows its location =>{node_2}')
#Here we print the value of node_2 is A
print(f'we print the value of node_2 is =>{node_2.data}')
#Here we print its next node, but it is None as we declared
print(f'we print its next node of node_2 => {node_2.next}')
#Here we print the next data node that is node_2 as we wrote up
print(f'we print the next data node of node_3 {node_3.next.data}')
#Here we changed the value of node_1 and now is C and its pointer is to node_3
node_1 = Node("C", node_3)
#Here we print the next data value that is node_3 B
print(f'We print the next data value of node_1 after be changed {node_1.next.data} \n \n')

'''

head = None
for count in range(1, 5):
    head = Node(count, head)
    head = head.next



while head != None:
    print(f"data: {head.data}, next: {head.next}")
    head = head.next
    