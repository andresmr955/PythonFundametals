import time

def timer(func):
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} started')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} took {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished slow function")

slow_function()
