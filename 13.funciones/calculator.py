import sys
##Crear una calculadora en una clase y poderla instanciar

print("Welcome to your favorite calculator!!!")

def input_User():
    user_choice = input('''
    Please chose which operation you want to do:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit        
    
''')
    return user_choice


def addition(a, b):
            return a + b 
def subtraction(a, b):
        return a - b 
def multiply(a, b):
        return a * b 
def divide(a, b):
    if b == 0:
        print("It is not possible to divide by 0")
    else: 
        return a / b     

while True:
    
        resultado = input_User()  

        if resultado == "5":
            print("Thanks for using the best calculator")
            break

        if resultado in ["1","2","3","4"]:
            while True:
                try:
                    num_One = float(input("Which is the first number you want to operate: => "))
                    num_Two = float(input("Which is the second number you want to operate: => "))

                    if resultado == "1":
                            result = f'The sum of {num_One} plus {num_Two} equal to {addition(num_One, num_Two)}'
                                                  
                    elif resultado == "2": 
                            result = f'The subtraction of {num_One} minus {num_Two} equal to {subtraction(num_One, num_Two)}'
                            
                            
                    elif resultado == "3":
                            result = f'The multiplication of {num_One} times {num_Two} equal to {multiply(num_One, num_Two)}'
                            
                                    
                    elif resultado == "4":
                                    if num_Two == 0:
                                        print("It is not possible to divide by 0")
                                        break
                                    result = f'The division of {num_One} by {num_Two} equal to {divide(num_One, num_Two)}'
                    print(result)
                    continue_required = input("Would you want to close the program Y/N: => ").strip().lower()
                    if continue_required == "y":
                        sys.exit()
                    else: 
                        break    
                except ValueError:
                       print("Value error, please enter a number")            
        else:
                print("Incorrect value")
                
  
    