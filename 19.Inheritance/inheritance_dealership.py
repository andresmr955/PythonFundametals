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
            print(f'The vehicle {self.brand} has been sold')
        else:
            print(f'The vehicle is not available')

##ABSTRACTION
    def check_available(self):
        return self.is_available
    def get_price(self):
        return self.price
    def start_engine(self):
        raise NotImplementedError("This method has to be implemented by subclass child")
    
    def stop_engine(self):
        raise NotImplementedError("This method has to be implemented by subclass child")


##The syntax to say that a subclass inherit from a parent class 
##INHERITANCE
class Car(Vehicle):
    #POLYMORPHISM
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
        

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The bike {self.brand} is rolling"
        else:
            return f"he bike {self.brand} is not available"
    
    def stop_engine(self):
        if self.is_available:
            return f"he bike {self.brand} has stopped"
        else:
            return f"he bike {self.brand} is not available"
        

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The truck's motor {self.brand} is rolling"
        else:
            return f"he truck's motor {self.brand} is not available"
    
    def stop_engine(self):
        if self.is_available:
            return f"he truck's motor {self.brand} has stopped"
        else:
            return f"he truck's motor {self.brand} is not available"
        

class Customer:
    def __init__(self, name):
        self.name = name 
        self.purchased = []

##This part is important because we used a vehicle class parent
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased.append(vehicle)
        else:
            print(f'Sorry this vehicle {vehicle} is not available')
    
    def check_available_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Available"
        else: 
            availability = "Not Available"
        print(f'The vehicle {vehicle.brand} is {availability} and costs {vehicle.get_price()}')

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle:Vehicle):
        self.inventory.append(vehicle)
        print(f'The vehicle {vehicle.brand} has been added to the inventory')

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'The customer {customer} has been registered')   

    def show_vehicles_available(self):
        print(f'Vehicles available in the store')
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} and the price is {vehicle.get_price()}")


car1 = Car("Toyota", "Corrolla", 2000)
bike1 =Bike("Yamaha", "MT-09", 7000)
truck1 = Truck("Volvo", "FH16", 8000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

##Show available vehicles

dealership.show_vehicles_available()

## customer wants to check a vehicle

customer1.check_available_vehicle(car1)

##customer wants to buy a car
customer1.buy_vehicle(car1)

##Show available vehicles

dealership.show_vehicles_available()