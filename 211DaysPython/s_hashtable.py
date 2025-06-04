class ContactList:
    def __init__(self, size):
        # Tu código aquí 👇
        self.size = size
        self.data = [[] for _ in range(size)]
    
    def __str__(self):
        return f"my contact {self.data}"
        
    def hash(self, key):
        # Tu código aquí 👇
        total = 0
        for char in key:
            total += ord(char)
        
        return total % self.size

    def insert(self, name, phone):
        # Tu código aquí 👇

        index = self.hash(name)
        bucket = self.data[index]
        
        for i, contact in enumerate(bucket):
            if contact[0] == name:
                bucket[i] = [name, phone]
                return True

        bucket.append([name, phone])
        return True

    def get(self, name):
        # Tu código aquí 👇

        index = self.hash(name)
        bucket = self.data[index]
        
        for i, contact in enumerate(bucket):
            print(contact[0])
            if contact[0] == name:
                return contact[1]
        return None

    def retrieveAll(self):
        # Tu código aquí 👇
        return self.data

    def delete(self, name):
        # Tu código aquí 👇

        index = self.hash(name)
        bucket = self.data[index]
        for i, contact in enumerate(bucket):
            if contact[0] == name:
                del bucket[i]
                return True
        return None
        
    def showBuckets(self):
        for i, bucket in enumerate(self.data):
            print(f"Bucket {i}: {bucket}")
            
my_contact = ContactList(5)
my_contact.insert("Andres" , 123456)
my_contact.insert("Angie" , 987654)
my_contact.insert("Paula" , 987654)
my_contact.showBuckets()
print("get", my_contact.get("Andres"))
print("retrieve", my_contact.retrieveAll())
print("get",my_contact.get("Angie"))
print("delete", my_contact.delete("Angie"))
print("get", my_contact.get("Angie"))
print("hash", my_contact.hash("Andres"))
