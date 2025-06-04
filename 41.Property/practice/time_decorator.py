import time
import functools

def decoration(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{func.__name__}]")
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"    () returned {result}")
        end_time = time.time()

        total_time = end_time - start_time
        print(f"    Total time = {total_time}")        
        return result
    return wrapper
@decoration
def sum(a, b):
    return a + b
a = 1 
b = 2
for _ in range(0, 3):
  
    sum(a, b)
    a += 1
    b += 1


def log(level):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level} Calling {func.__name__}]")
            result = func(*args, **kwargs);
            print(f"     ()returned {result}")
            return result
        return wrapper
    return decorator              

@log(level="WARNING")
def add (a, b):
    return a * b
print(add(5,5))