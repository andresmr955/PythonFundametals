from node import Node
head = None
head = Node("K", head)
head = Node("L", head)
head = Node("M", head)
head = Node("N", head)

print("Original List:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

##How to add in any place of the linked list

index = 8

if index <= 0 or head.next is None:
    removed_item = head.data
    head = head.next
    print(f'item removed {removed_item}')
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -=1
    removed_item = probe.next.data
    probe.next = probe.next.next
    print(f'item removed {removed_item}')

    

print("\nList after adding:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")