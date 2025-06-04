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

#How to delete an item at the beginning


# Delete the item at the beginning
if head is not None:
    removed_item = head.data
    head = head.next  # Move head to the second node
    print(f"\nRemoved item from the beginning: {removed_item}")

print("\nList after deletion:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")