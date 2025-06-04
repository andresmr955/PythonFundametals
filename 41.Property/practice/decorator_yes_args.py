import functools

def parametrized_decorator(message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{message} - Before executing {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{message} - After executing {func.__name__}")
            return result
        return wrapper
    return decorator  # Returns the actual decorator

@parametrized_decorator("LOG")
def greet(name):
    print(f"Hello, {name}")
