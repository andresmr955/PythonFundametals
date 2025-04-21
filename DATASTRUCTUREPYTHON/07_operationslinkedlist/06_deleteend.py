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


removed_item = head.data
print(removed_item)


if head is None:
    print("List is empty, cannot delete.")
elif head.next is None:
    head = None
else:
    probe = head 
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next.data
    probe.next = None
print(removed_item)

print("\nList after deletion:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")