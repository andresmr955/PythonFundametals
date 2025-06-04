def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Example usage:

if __name__ == '__main__':
    try:
        print(add(10, 5))             # Addition: 15
        print(subtract(10, 5))        # Subtraction: 5
        print(multiply(10, 5))        # Multiplication: 50
        print(divide(10, 0))          # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
