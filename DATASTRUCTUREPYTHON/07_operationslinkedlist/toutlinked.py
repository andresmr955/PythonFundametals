from node import Node

# How to make a single link list tour?

head = None
#We create different nodes because we iterate a range between 1 to 6
for count in range(1,6):
    head = Node(count, head)

print("First Tour:")
#Here we iterate with a while loop starting from five to one
current = head  # Use a separate pointer 'current' for the first traversal
while current != None:
    print(current.data)
    current = current.next

# To make a "tour", reset a pointer back to the head
probe = head

print("\nSecond Tour:")
# Now 'probe' starts at the beginning of the list again
while probe != None:
    print(probe.data)
    probe = probe.next