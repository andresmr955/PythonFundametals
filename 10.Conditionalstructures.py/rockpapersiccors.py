import random

def game(x):
    player = 0
    machine = 0



    while player < 3 and  machine < 3:
            
            
            machine_choice = random.randint(1,3)
            customer_election = ""
            machine_election = ""
            
            if x == 1:
                customer_election = "rock"
            elif x == 2:
                customer_election = "paper"
            elif x == 3:
                customer_election = "scissors"  

            if machine_choice == 1:
                machine_election = "rock"
            elif machine_choice == 2:
                machine_election = "paper"
            elif machine_choice == 3:
                machine_election = "scissors" 

            print(f'Your choice {customer_election} and the machine choice {machine_election}')
           
            if x == 1 and machine_choice == 3:
                player += 1
                print("You win")
            elif x == 2 and machine_choice == 1:
                player += 1
                print("You win")
            elif x == 3 and machine_choice == 2:
                player += 1
                print("You win")
            elif x == machine_choice:
                print("It is a Draw")    
            else:
                machine += 1
                print("Machine wins")
                      
            if player == 3 or machine == 3:
                break   
            
            x = int(input("Choice again => "))
    if player == 3:
        print(f'Congratulations 🍾🎉 You won the game') 
    elif machine == 3:
        print(f'Machine 🤖 won the game')           
    

while True:
    try:
        customer_choise = int(input('''Welcome to the game!!
                Please chose a rock(1), paper(2), scissors(3): => '''))
    except ValueError:
        print("Invalid input, please enter a number 😡")
        if customer_choise in [1, 2, 3]:  # Validación de la elección del jugador
            break  # Si la entrada es válida, salimos del bucle
        else:
            print("Invalid input, please choose a valid option: rock(1), paper(2), or scissors(3).")

game(customer_choise)

