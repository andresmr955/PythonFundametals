from typing import Optional, Union, Dict

def calculate_total(*args: Union[int, str, float], discount: Optional[float] = None, **kwargs: Dict[str, float]) -> float:
    print(f"Positional args: {args}, Named args: {kwargs}, Discount: {discount}")

    """
    Calculates the total sum of numeric positional and keyword arguments, and applies a discount if provided.
    Parameters:
    ________________

    *args: Union[int, str, flat]
        Positional arguments which may includes numbers, or other types. Only numeric values are summed.
    discount: Optional[Float], default=None
        A percentage discount to apply to the total sum. If None, no discount is applied.
    **kwargs: Dict[str, float]
        Keywords arguments with string keys and numeric values. Only numeric values are summed

    Returns:
    ____
    Float
    The final total after applying the discount (if any)

    """
    valid_args = [arg for arg in args if isinstance(arg, (int, float))]
    total_args = sum(valid_args)

    total_kwargs = sum(value for value in kwargs.values() if isinstance(value, (int, float)))
    total = total_args + total_kwargs

    if discount is not None:
        print(f"There is a {discount}% discount")
        total_discount = (total * discount) / 100
        total -= total_discount
        return f"Total with discount: => :) {total}"
        
    else:
        print("No discount available")
        return f"Total without discount: {total}"
    
products = ["phone", "tv", "pc", "car"]
prices = [1000, 2000, 8000, 30000]
cart_shopping = dict(zip(products, prices))

print(calculate_total(1000, 2000, 3000, "chair", *prices, bottle=400, **cart_shopping, house=500, discount=10))