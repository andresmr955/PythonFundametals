class Car:
    def __init__(self, brand, model, year, mileage):
        # Tu código aquí 👈
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.state = False

    def turnOn(self):
        self.state = True
        return self.state
      
    def turnOff(self):
        self.state = False
        return self.state
    def drive(self, kilometers):
        if self.state == True:
            self.mileage += kilometers
            print(self.mileage)
        else:
            raise Exception("El carro esta apagado")

toyota = Car("Toyota", "Corolla", 2020, 0)
toyota.turnOn()
toyota.drive(100)
toyota.mileage