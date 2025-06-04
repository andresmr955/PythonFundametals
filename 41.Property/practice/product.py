class Product:
    def __init__(self, price, name):
        self.name = name
        self._price = price
        self.stock = False
        self._quantity = 0

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Price can not be negative")

    @price.deleter
    def price(self):
        if self.quantity == 0:
            del self._price
            del self.stock
        else:
            raise ValueError("We can not delete price if there is stock")
        
    def __repr__(self):
        return f'The product:{self.name}, costs {self._price} and there are {self._quantity} in stock'
    
    def __str__(self):
        return f"{self.name} - ${self._price} - Stock: {self._quantity}"