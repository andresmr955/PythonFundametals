

def calculator():
    while True:
        try: 
            first_number = int(input("Please enter the first number you want operate: "))
            second_number = int(input("Please enter the second number you want operate: "))
            operator = input("Please enter the operator (+, -, *, /): ")

            if not operator in ["+", "-", "*", "/"]:
                print("It is not an operator")
                continue
                

            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "*":
                result = first_number * second_number
            elif operator == "/":
                result = first_number / second_number
            print(result)    
        except ZeroDivisionError as e:
            print("You can not divide by zero", e)
        except ValueError as e:
            print("Please enter an integer number: ", e)
        except KeyError as e: 
            print("Please enter a real operator: ", e)
            
    
print(calculator())