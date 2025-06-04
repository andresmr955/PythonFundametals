from node import Node
head = None
head = Node("K", head)
head = Node("L", head)
head = Node("M", head)

print("Original List:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

##How to add in any place of the linked list

new_item = "Z"
index = 2
counter = 0
current = head

while current != None and counter < index:    
    previous = current
    current = current.next
    counter += 1
if counter == index:
    new_node = Node(new_item, current)
    previous.next = new_node
else:
    print(f"Index {index} out of bounds for list of length {counter}")



    

print("\nList after adding:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")