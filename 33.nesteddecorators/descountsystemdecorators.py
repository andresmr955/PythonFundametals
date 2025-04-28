import time 

customer1 = {"name": "Alice", "type": "VIP"}
customer2 = {"name": "Bob", "type": "regular"}

cart1 = [50, 30, 20]  # Total = 100
cart2 = [70, 40, 30]  # Total = 140

def discount(func):
    def wrapper(user, cart):
        if user.get('type') != 'VIP':
            return f"there is not discount"
        else:
            cart_updated = []
            for purchase in cart:
                discount = (purchase * 20) / 100
                purchase -= discount
                cart_updated.append(purchase)
        return func(user, cart_updated)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return f'The result is {result} and the time taken {end_time - start_time:.4f}'
    return wrapper
@timer
@discount
def calculate_total(customer, cart):
    return f"The total of your cart {customer.get('name') }is {sum(cart)}"

print(calculate_total(customer1, cart1))
print(calculate_total(customer2, cart2))  # Regular customer
