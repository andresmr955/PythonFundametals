class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self._price = price
        self._quantity = quantity
        self.category = category

    @property
    def get_value_stock(self):
        return self.price * self.quantity
    
    @property 
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("The price must be a positive number")

    @property
    def stock(self):
        return self._quantity 
    
    @stock.setter
    def stock(self, new_quantity):
        if new_quantity >= 0:
            self._quantity = new_quantity
        else:
            raise ValueError("The quantity must be positive number")
    
    
    @property
    def total_value(self):
        return self.price * self._quantity

    
    def __repr__(self):
        return f"Product(name: {self.name}, price: {self._price}, quantity: {self._quantity}, category: {self.category}, total_value: {self.total_value})"

class Inventory:
    def __init__(self):
         self._products = []

    @property
    def stock(self):
        return self._products
    
    @stock.setter
    def stock(self, new_product):
        self.products.append(new_product)
        return self.products
    
    @stock.deleter
    def stock(self):
        if self._products == []:
            del self._products

    def add_products(self, product):
        self._products.append(product)

    def find_products(self, product_required):
        return [product['name'] for product in self._products if product == product_required]

    def rmv_products(self, product_required):
        for product in self._products:
            if product == product_required:
                self._products.remove(product)
                print(f"Item: {product.name} removed")
                return 0
            else:
                print("Product not found")

    def generate_inform(self):
        with open('inform.txt', mode='a') as file:
            for product in self._products: 
                file.write(f" Product: {product.name}")
    def __str__(self):
        return f"Inventory({len(self._products)} products)"
    

p1 = Product("Laptop", 1000, 5, "Electronics")
p2 = Product("Smartphone", 500, 10, "Electronics")
p3 = Product("Shoes", 80, 15, "Clothing")

# Crear inventario
inventory = Inventory()

# Añadir productos al inventario
inventory.add_products(p1)
inventory.add_products(p2)
inventory.add_products(p3)

# Ver el inventario
print(inventory)

# Encontrar productos por nombre
found_products = inventory.find_products("Laptop")
print(found_products)

# Remover un producto
inventory.rmv_products("Smartphone")

# Generar reporte del inventario
inventory.generate_inform()

# Ver el inventario después de la eliminación
print(inventory)