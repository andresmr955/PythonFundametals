
def log_transaction(func):
    def wrapper():
        print("1. Log transaction...")
        func()
        print("3. Log finished!")
    
    return wrapper

@log_transaction
def process_payment():
    print("2. Processing payment")

process_payment()