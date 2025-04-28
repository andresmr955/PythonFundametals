from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    #Create a dictionary with a value 0 by default
    product_count = defaultdict(int)
    for order in orders:
        product_count[order] += 1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
result = count_products(orders)
print(result)  # Output: defaultdict(<class 'int'>, {'laptop': 2, 'smartphone': 1, 'tablet': 1})