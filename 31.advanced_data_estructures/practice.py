# Implement a system for managing orders

#1. Use defaultdicts to keep track of each product we have
#2. Use enumeration to see the order status: pending, shipped, delivered
#3. Counter to make a count of each product

from collections import defaultdict, Counter
from enum import Enum
import random


products_list = [
    'apple', 'banana', 'orange', 'pear', 'grape', 'apple', 'apple', 'orange', 'pear', 'banana',
    'kiwi', 'mango', 'melon', 'watermelon', 'cherry', 'kiwi', 'mango', 'melon', 'watermelon', 'cherry',
    'apple', 'banana', 'orange', 'pear', 'grape', 'apple', 'banana', 'orange', 'pear', 'grape',
    'raspberry', 'blueberry', 'lemon', 'lime', 'grapefruit', 'raspberry', 'blueberry', 'lemon', 'lime', 'grapefruit',
    'apple', 'banana', 'orange', 'pear', 'grape', 'apple', 'banana', 'orange', 'pear', 'grape',
    'kiwi', 'mango', 'melon', 'watermelon', 'cherry', 'kiwi', 'mango', 'melon', 'watermelon', 'cherry',
    'raspberry', 'blueberry', 'lemon', 'lime', 'grapefruit', 'raspberry', 'blueberry', 'lemon', 'lime', 'grapefruit',
    'apple', 'banana', 'orange', 'pear', 'grape', 'apple', 'banana', 'orange', 'pear', 'grape',
    'kiwi', 'mango', 'melon', 'watermelon', 'cherry', 'kiwi', 'mango', 'melon', 'watermelon', 'cherry',
    'raspberry', 'blueberry', 'lemon', 'lime', 'grapefruit', 'raspberry', 'blueberry', 'lemon', 'lime', 'grapefruit'
]

def register_products(orders: list[str], fixed_status_param: dict[str, str]) -> list[dict]:
    product_count = defaultdict(int)


    for product in orders:
        product_count[product] += 1

    result = []

    for product, count in product_count.items():
        result.append(
            {
                'product': product,
                'count' : count,
                'status': fixed_status_param[product]
            }
        )
    return result


def add_status(product_list_param):
    statuses = [OrderEnumeration.PENDING.name, OrderEnumeration.SHIPPED.name, OrderEnumeration.DELIVERED.name]
    fixed_statuses = {}

    for product in set(product_list_param):
        fixed_statuses[product] = random.choice(statuses)

    return fixed_statuses

#print(register_products(products_list, add_status(products_list)))

class OrderEnumeration(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3


def check_status(list_of_dict, product_name):

    for product_info in list_of_dict:
        if product_info['product'] == product_name:
            if product_info['status'] == OrderEnumeration.PENDING.name:
                return f" {product_info['product']} Order is still pending"
            elif product_info['status'] == OrderEnumeration.SHIPPED.name:
                return  f" {product_info['product']} Order is still shipped"
            elif product_info['status'] == OrderEnumeration.DELIVERED.name:
                return  f" {product_info['product']} Order is delivered"


def counter_func(products_list: list[str]) -> Counter:
    return Counter(products_list)

dict_with_status_fixed = register_products(products_list, add_status(products_list))
print(check_status(dict_with_status_fixed, 'lemon'))
print(counter_func(products_list))
print(dict_with_status_fixed)