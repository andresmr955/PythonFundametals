##concecionario
# comprar y vender
# vehiculos
#usuario va poder 
#cual es ta disponible 
#cual es su precio
#comprar uno


class Car:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.car_available = True
        self.car_on = False

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

class Client:
    def __init__(self, name, phone_number):
        self.name = name 
        self.phone_number = phone_number
        self.user_car = []

    def __str__(self):
        pass
    def __repr__(self):
        return self.__str__()
    
    def client_buy(self, car):
       self.user_car.append(car)
       print(f'The user has bought     the car')
        
class Dealership:
    def __init__(self):
        self.cars = []
    
    def buy_cars(self, car):
        if car in self.cars:
            print(f'This car {car} is already added')
        else:   
            self.cars.append(car)
            print(f'This car is added to the dealership')
            print(f'The list of cars {self.cars}')
    def sell_cars(self, car, client):
        if car.car_available:
            self.cars.remove(car.brand)
            client.client_buy(car.brand)
            print(f'The car is sold to you, your cars are {client.user_car}')
            print(f'The list of cars {self.cars}')
        else: 
            print("The car can not be sold")
    def know_price(self, car):
        if car in self.cars:
            print(f'The price of the {car.brand} is {car.price}')
        else:
            print("We do not have this car")


car1 = Car(1500, "Toyota")
car2 = Car(8000, "Hyunday")
car3 = Car(600, "Ferrari")
car4 = Car(20000, "BMW")
client1 = Client("Andres", 123)

car1.run()
car1.stops()
car1.stops()

dealership = Dealership()
dealership.buy_cars(car1)
dealership.buy_cars(car2)
dealership.buy_cars(car3)
dealership.buy_cars(car4)

dealership.know_price(car4)

dealership.sell_cars(car2, client1)
dealership.know_price(car2)
