from functools import reduce

numbers = [1, 2, 3, 4, 5]

def accum(counter, item):
    print(f'counter: => {counter}')
    print(f'item: => {item}')
    return counter + item

result = reduce(accum, numbers)

#result = functools.reduce(lambda counter,  item: counter + item, numbers)
print(result)


productos = [
    {"manzana": 1.5},
    {"banana": 2.0},
    {"pera": 1.2},
    {"uva": 3.0}
]

total_products = reduce(lambda accum, actual: {**accum, **actual}, productos)
print(total_products)