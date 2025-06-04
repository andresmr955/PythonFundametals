class Product():
    def __init__(self, price: float, stock: float):
        self.__price = price
        self.__stock = stock

    @property 
    def product_price(self):
        return self.__price
  
    @product_price.setter
    def product_price(self, value:float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("The number should be positive")
        self.__price = value
     
    
    @property 
    def product_stock(self):
        return self.__stock
    
    @product_stock.setter
    def product_stock(self, value: float) -> float:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Please try a positive number")
        self.__stock = value
      
    
    @product_price.deleter
    def product_price(self):
        del self.__price
    
    @product_stock.deleter
    def product_stock(self):
        del self.__stock

my_prod = Product(200, 4)

# Use
my_prod = Product(200, 4)
print(my_prod.product_price)  # ✅ sin paréntesis
print(my_prod.product_stock)

# Change values
#my_prod.product_price = -400

my_prod.product_price = 300
my_prod.product_stock = 10

# Delete
del my_prod.product_price
del my_prod.product_stock