





#How to insert a new element in our nodes

def insert_new(head):
    new_node = Node("F")

    if head is None:
        head = new_node
    else:
        probe = head
        
        while probe.next != None:
            probe = probe.next
        probe.next = new_node

    print(head.data)

    
head = None
insert_new(head)
head = Node("K", head)
insert_new(head)

while head != None:
    print(f"This is the last head {head.data}")
    head = head.next
