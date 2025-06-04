import functools

def log(level):
    def decorator(func):
        @functools.wraps(func)  # Preserves function name and docstring
        def wrapper(*args, **kwargs):
            print(f"[{level}] Calling {func.__name__}()")
            result = func(*args, **kwargs)
            print(f"[{level}] {func.__name__}() returned {result}")
            return result
        return wrapper
    return decorator  # Returns the actual decorator

# Example usage:
@log(level="WARNING")
def add(a, b):
    return a + b

print(add(3, 5))
