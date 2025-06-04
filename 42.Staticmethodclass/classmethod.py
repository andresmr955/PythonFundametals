class Order:
    global_discount = 10 #necessary  1

    def __init__(self, amount):
        self.amount = amount

    @classmethod #necessary 2 
    def update_discount(cls, new_discount):
        print(cls.global_discount)
        cls.global_discount = new_discount #necessary 3
        return cls.global_discount
    
print(Order.update_discount(15))
print(Order.global_discount)