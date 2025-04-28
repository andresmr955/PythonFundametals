def logger(func):
    def wrapper(args, **kwargs):
        try: 
            result = func(args, **kwargs)
            with open('./33.nesteddecorators/loggerpractice.txt',  mode='a') as file:
                file.write(f'{result}\n')
            return result
        except Exception as e:
            print(f"Error: {e}")
    return wrapper
    

def authenticator(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('is_authenticated', False) :
            return "Access denied"
        return func(user, *args, **kwargs)
    return wrapper


@logger
@authenticator
def view_account(user):
    return f'account details for {user["name"]}'

            # --- Ejemplo de uso:
user1 = {"name": "Alice", "is_authenticated": True}
user2 = {"name": "Bob", "is_authenticated": False}

view_account(user1)