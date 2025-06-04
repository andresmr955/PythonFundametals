from collections import defaultdict, Counter

def count_products(orders: list[str]) -> defaultdict:
    #Create a dictionary with a value 0 by default
    product_count = defaultdict(int)
    for order in orders:
        product_count[order] += 1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
result = count_products(orders)
print(result)  # Output: defaultdict(<class 'int'>, {'laptop': 2, 'smartphone': 1, 'tablet': 1})

#EXAMPLE 2 

def count_products_counter(products: list[str]) -> Counter:
    #Create a dictionary with a value 0 by default
    return Counter(products)

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
result_2 = count_products_counter(orders)
print(result_2)  # Output: defaultdict(<class 'int'>, {'laptop': 2, 'smartphone': 1, 'tablet': 1})

