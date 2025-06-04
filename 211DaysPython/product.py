class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
  
  def __str__(self):
        return f"name: {self.name}, price: ${self.price}, quantity: {self.quantity}"

  def __repr__(self):
      return self.__str__()
    
  def addToCart(self):
    raise NotImplementedError("La lógica de este método debe ser implementada por las clases hijas")

