def increment(x):
    """
    Incrementa el valor de x en 1.
    """
    return x + 1

def high_ord_func(x, funx):
    return x + funx(x)

result = high_ord_func(2, increment)
# 2 ( 2 + 1 ) = 5
print(result)  # Output: 11


higher_order_lambda = lambda x, function: x + function(x)

solution_v2 = higher_order_lambda(2, lambda x: x + 1)
print(solution_v2)