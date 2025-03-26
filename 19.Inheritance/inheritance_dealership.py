class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.mode = model
        self.price = price
        self.is_available = True

#The subclasses child are going to inherit all parameters that we are putting in the super Class

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'You can sell the car {self.brand}')
        else:
            print(f'The vehicle is not available')

    def check_available(self):
        return self.is_available
    def get_price(self):
        return self.price
    def start_engine(self):
        raise NotImplementedError("This method has to be implemented by subclass child")
    
    def stop_engine(self):
        raise NotImplementedError("This method has to be implemented by subclass child")


##The syntax to say that a subclass inherit from a parent class 

class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The car's motor {self.brand} is rolling"
        else:
            return f"he car's motor {self.brand} is not available"
    
    def stop_engine(self):
        if self.is_available:
            return f"he car's motor {self.brand} has stopped"
        else:
            return f"he car's motor {self.brand} is not available"
        

car1 = Car("chevrolet", 2012, 2500)

car1.sell()

car1.start_engine()