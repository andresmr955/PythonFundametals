def calculate_total(products, discount):
    total = 0
    for product in products:
        discount = (product["price"] * discount) / 100
        total += product["price"] - discount
    return total

def test_calculate_item():
    print("Works")
    assert calculate_total([{'Name': 'iphone', 'price': 100}], 20) == 80  
    print(calculate_total([{'Name': 'iphone', 'price': 100}], 50))
if __name__ == "__main__":
    test_calculate_item()