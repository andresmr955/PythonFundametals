class Animal:
    def __init__(self, name, age, specie):
        # Tu código aquí 👇
        self.name = name
        self.age = age
        self.specie = specie

    def getInfo(self):
       return {
          "name" : self.name, 
          "age" : self.age,
          "specie": self.specie
       }
    
class Mammal(Animal):
    def __init__(self, name, age, specie, hasFur):
    # Tu código aquí 👇
        super().__init__(name, age, specie)
        self.hasFur = hasFur
    
    def getInfo(self):
       info = super().getInfo()
       info["hasFur"] = self.hasFur
       return info

class Dog(Mammal):
    def __init__(self, name, age, breed, specie="dog", hasFur= True):
        super().__init__(name, age, specie, hasFur )
        self.breed = breed
    
    def bark(self):
        return 'woof!'
    
    def getInfo(self):
        info = super().getInfo()
        info["breed"] = self.breed
        
        return info

dog = Dog("fido", 4, "pastor aleman")
print(dog.getInfo())
print(dog.bark())