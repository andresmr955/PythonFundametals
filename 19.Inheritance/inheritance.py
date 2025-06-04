##concecionario
# comprar y vender
# vehiculos
#usuario va poder 
#cual es ta disponible 
#cual es su precio
#comprar uno


class Car:
    def __init__(self, price, brand, model):
        self.price = price
        self.brand = brand
        self.model = model
        self.car_available = False
        self.car_on = False

    def __str__(self):
        return f'{self.brand} {self.model}'
    def __repr__(self):
        return self.__str__()    

    def change_Price(self, price):
        if price == 0:
            print("You gotta update the price")
        else:
            price = input('Which is the new price? => ')
    
    def run(self):
        self.car_on = True
        print(f'Car {self.brand} is running...')
        
    def stops(self):
        if not self.car_on:
            print("Car is already stopped...")
        else:
            self.car_on = False
            print("Car is stopped")

    def check_availability_car(self):
        return self.car_available

class Client:
    def __init__(self, name, phone_number):
        self.name = name 
        self.phone_number = phone_number
        self.user_car = []
    
    def client_buy(self, car):
       self.user_car.append(car)
       print(f'The user has bought {car} the car')

    def inquire(self, check_car):
        if check_car.check_availability_car():
            print(f'The car {check_car} is available')
        else:
            print(f'The car {check_car.brand} {check_car.model} is not available')

class Dealership:
    def __init__(self):
        self.cars = []
        self.customers = []

    def __str__(self):
        return f"Customers: {self.customers}"
    
    def __repr__(self):
        return self.__str__()
    
    def buy_cars(self, car):
            car.car_available = True
            self.cars.append(car)
            print(f'This car {car.brand} {car.model} is added to the dealership')
            
    def register_customer(self, customer):
        
        if not customer in self.customers:
            self.customers.append(customer)
            print(f'The customer {customer.name} has been added')        
        else:
            print(f'The customer {customer.name} is already added')  

    def sell_cars(self, car, client):
        print(f'The list of cars {self.cars}')
        if car.car_available:
            client.client_buy(car)
            print(f'The car is sold to you, your cars are {client.user_car}')
            car.car_available = False
            self.cars.remove(car)
        else: 
            print(f'The car {car} can not be sold, because it is not available')
    
    def check_all_cars_available(self):
        print(f'The whole invenatary now is ')
        for car in self.cars:
            if car.check_availability_car():
                print(f'- {car.brand} {car.model} is available')

    def know_price(self, car):
        if car in self.cars:
            print(f'The car {car.brand} cots {car.price}')

##We create instances

car1 = Car(1500, "Toyota", 2015)
car2 = Car(8000, "Hyunday", 2020)
car3 = Car(600, "Ferrari", 2022)
car4 = Car(20000, "BMW" ,2025)
car5 = Car(20, "Mazda", 1999)

##We register the customer

client1 = Client("Andres", 123)


car1.run()
car1.stops()
car1.stops()

dealership = Dealership()

dealership.buy_cars(car1)
dealership.buy_cars(car2)
dealership.buy_cars(car3)
dealership.buy_cars(car4)

dealership.register_customer(client1)

dealership.know_price(car4)
##Customer wants to know if these cars are available

client1.inquire(car4)
client1.inquire(car5)


dealership.check_all_cars_available()
dealership.sell_cars(car4, client1)
dealership.check_all_cars_available()

dealership.sell_cars(car4, client1)
