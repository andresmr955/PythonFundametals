from product import Product
class Article(Product):
  
  def addToCart(self):

    return f"Agregando {self.quantity} unidades del articulo {self.name} al carrito"
  
class Service(Product):
  def addToCart(self):
    # Tu código aquí 👈
    return f"Agregando el servicio {self.name} al carrito"
  
class Cart:
  def __init__(self):
   
    self.shopping = []
  
  def addProduct(self, product):
   
    self.shopping.append(product)
    return product.addToCart()
  
  def deleteProduct(self, product):
        for item in self.shopping:
            if product.name == item.name:
                self.shopping.remove(item) 
                return self.shopping
  
        
  def calculateTotal(self):
        
    return [sum(quantity.quantity * quantity.price for quantity in self.shopping)]
  
  def getProducts(self):
    return [item for item in self.shopping]
  

if __name__ == '__main__':
    # Crear productos
    book = Article(name="Libro", price=100, quantity=2)  # 2 libros a 100 cada uno
    course = Service(name="Curso", price=120, quantity=1)  # 1 curso a 120

    print(isinstance(book, Product))  # Esto debería devolver True
    print(isinstance(course, Product))  # Esto debería devolver True
    # Crear carrito
    cart = Cart()

    # Agregar productos al carrito
    print(cart.addProduct(book))  # Debería agregar el libro
    print(cart.addProduct(course))  # Debería agregar el curso

    # Mostrar productos en el carrito
    print("\nProductos en el carrito:")
    print(cart.getProducts())

    # Eliminar un producto del carrito
    print("\nEliminando un producto...")
    cart.deleteProduct(book)
    print(cart.getProducts())

    # Ver el total después de eliminar un producto
    print("\nNuevo total del carrito:")
    print(cart.calculateTotal())
