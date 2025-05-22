import time
import functools

def log_execution(func):
    @functools.wraps(func)  # Preserve function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        
        result = func(*args, **kwargs)  # Execute the function
        
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate runtime
        
        num_args = len(args) + len(kwargs)  # Count arguments

        # Logging details
        print(f"[LOG] Executed '{func.__name__}'")
        print(f"    - Execution time: {execution_time:.6f} seconds")
        print(f"    - Number of arguments: {num_args}")
        print(f"    - Return value: {result}")
        
        return result

    return wrapper

# Example usage:
@log_execution
def add(x, y):
    return x + y

print(add(3, 5))

