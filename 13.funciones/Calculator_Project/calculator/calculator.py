##Crear una calculadora en una clase y poderla instanciar

import sys

from calculator.operations import addition, subtraction, multiply, divide

class Calculator:
        def __init__(self):
            print("Welcome to your favorite calculator!!!")
      


        def input_User(self):
            return input('''
            Please chose which operation you want to do:
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Exit        
            
        ''')

        def get_number(self):
            while True: 
                try:
                    self.num_one = float(input("Which is the first number you want to operate: => "))
                    self.num_two = float(input("Which is the second number you want to operate: => "))
                    return self.num_one, self.num_two
                except ValueError:
                       print("Value error, please enter a number")     

        def run(self):
            while True:
    
                choice = self.input_User()

                if choice == "5":
                    print("Thanks for using the best calculator")
                    sys.exit()

                if choice in ["1","2","3","4"]:
                    self.get_number()
                    while True:

                            try: 
                                if choice == "1":
                                    result = f'The sum of {self.num_one} plus {self.num_two} equal to {addition(self.num_one, self.num_two)}'
                                                        
                                elif choice == "2": 
                                        result = f'The subtraction of {self.num_one} minus {self.num_two} equal to {subtraction(self.num_one, self.num_two)}'
                                        
                                        
                                elif choice == "3":
                                        result = f'The multiplication of {self.num_one} times {self.num_two} equal to {multiply(self.num_one, self.num_two)}'
                                        
                                                
                                elif choice == "4":                                
                                    result = f'The division of {self.num_one} by {self.num_two} equal to {divide(self.num_one, self.num_two)}'
                                
                                print(result)
                                
                            except ValueError as e:
                                 print(e)

                            continue_required = input("Would you want to close the program Y/N: => ").strip().lower()
                            if continue_required == "y":
                                print("Thanks 🫂 for CHOSING the best calculator🧮 ")
                                sys.exit()
                            else: 
                                break    
                            
                else:
                    print("Incorrect value, please enter a number from 1 to 5")
                        
    
        