class ContactList:
    def __init__(self, size):
        # Tu código aquí 👇
        self.size = size
        self.data = [[] for in range(self.size)]
    
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
        self.data.append([name, phone])
        return True

    def get(self, name):
        # Tu código aquí 👇
        for contact in self.data:
            if contact[0] == name:
                return contact[1]
        return None

    def retrieveAll(self):
        # Tu código aquí 👇
        return self.data

    def delete(self, name):
        # Tu código aquí 👇
        for i, contact in enumerate(self.data):
            if contact[0] == name:
                del self.data[i]
                return True
        return None
        

my_contact = ContactList(5)
my_contact.insert("Andres" , 123456)
my_contact.insert("Angie" , 987654)
print("get", my_contact.get("Andres"))
print("retrieve", my_contact.retrieveAll())
print("get",my_contact.get("Angie"))
print("delete", my_contact.delete("Angie"))
print("get", my_contact.get("Angie"))
print("hash", my_contact.hash("Andres"))