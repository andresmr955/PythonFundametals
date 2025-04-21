from node import Node

# How to search an element and replaced for an item in the linked list?

head = None
new_item = "Z"

for count in range(1,6):
    head = Node(count, head)

probe = head
target_item = 3

while probe != None and target_item != probe.data:
    print(probe.data)
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f"{new_item} replaced the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")