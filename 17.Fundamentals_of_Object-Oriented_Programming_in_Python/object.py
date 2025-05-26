class Car():
    def __init__(self):
        self.color = "Blue"
        self.brand = "toyota"
        self.year = 2025

    def __str__(self):
        return "{self.color}-{self.brand}-{self.year}"
    
car = Car()
print(car.__dict__)