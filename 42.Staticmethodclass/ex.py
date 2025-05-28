class Order:
    global_discount = 10 #necessary  1
    global_price = 100

    def __init__(self, amount, price):
        self.amount = amount
        self.price = price

    @classmethod #necessary 2 
    def update_discount(cls, new_discount):
        print(cls.global_discount)
        cls.global_discount = new_discount #necessary 3
        return cls.global_discount
    
    @staticmethod
    def verify_amount(amount, minimum= 50):
        if amount > minimum:
            print(f'The order amount {amount} is allowed (greater than {minimum})')
            return True
        else:
            print(f'The order amount {amount} is NOT allowed (must be greater than {minimum})')
            return False
        
    @classmethod
    def create_order_with_discount(cls, amount):

        if cls.verify_amount(amount):
            print("creating order")
            discount = (amount * cls.global_discount) / 100
            price_after_discount = cls.global_price - discount
            print("order created")
            return cls(amount, price_after_discount)
        else:
            print("Order not created due to restrictions")
            return False
        
        
        


print(Order.update_discount(15))
print(Order.global_discount)

Order.verify_amount(60)              # Verifica si 60 es válido
order = Order.create_order_with_discount(60)  # Crea un pedido aplicando descuento
print(order.amount)
print(order.price)

Order.verify_amount(30)              # Verifica si 30 es válido
order2 = Order.create_order_with_discount(30) # No debería crear pedido