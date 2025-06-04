
class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}
class MySingleLinkedList{
    constructor(value){
        this.head = {
            value: value,
            next: null, 
        };
        this.tail = this.head;
        this.length = 1;
    }
    append(value){
        const newNode = new Node(value)

        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }

    prepend(value){
        const newNode = new Node(value)

        newNode.next = this.head;
        this.head = newNode
        this.length++;
        return this;
    }

    insert(index, value){
        
        if (index >= this.length){
            return this.append(value)

        }
        
        const newNode = new Node(value)
        const firstPointer = this.getTheIndex(index - 1)
        const holdingPointer = firstPointer.next

        firstPointer.next = newNode;
        newNode.next = holdingPointer;
        this.length++;

        return this;
    }

    delete(index){
        if(index >= this.length || index < 0){
            console.log(`Cannot delete index ${index}, it does not exist`);
            return;
        }
        
        if(index===0){
            this.head = this.head.next;
            this.length--;
            return this
        }

        const holdingPointer = this.getTheIndex(index - 1)

        const deleteNode = holdingPointer.next
        
        holdingPointer.next = deleteNode.next

        if(index === this.length - 1){
            this.tail = holdingPointer;
        }
    
        this.length--;

    }

    getTheIndex(index){
        let counter = 0
        let currentNode = this.head;
        
        while(counter !== index){
            currentNode = currentNode.next
            counter++;
        }
        return currentNode
    }
}

let myLinkedList = new MySingleLinkedList(1);

myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)
myLinkedList.prepend(6)
myLinkedList.insert(3, 8)
console.log(myLinkedList)
myLinkedList.delete(4)
console.log(myLinkedList)
console.log(JSON.stringify(myLinkedList, null, 2))
