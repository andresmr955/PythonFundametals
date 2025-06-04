from node import Node

# How to search for an item in the linked list?

head = None

probe_class = head
target_item = 2

while probe_class != None and target_item != probe_class.data:
    probe_class = probe_class.next

if probe_class != None:
    print(f"Target item {target_item} has been found")
else:
    print(f"Target item {target_item} is not in the list")
#MINUTE 5:12