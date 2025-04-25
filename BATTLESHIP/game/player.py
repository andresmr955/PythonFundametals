from ship import Destroyer, Submarine, Battleship


class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.attack_board = [[" " for _ in range(10)] for _ in range(10)]

    def place_ships(self):
        ships_to_place = [("Destroyer", Destroyer()), ("Submarine", Submarine()), ("Battleship", Battleship())]

        for name, ship in ships_to_place:
            start_row, start_col, direction = self.ask_start_row__start_col(name)
            while not ship.place_ship(self.board, start_row, start_col, direction): 
                start_row, start_col, direction = self.ask_start_row__start_col(name)     

                if ship.place_ship(self.board, start_row, start_col, direction):
                    self.ships.append(ship)
                    break
                else:         
                    print(f"Try again for the {name}.")
            
            
    def print_board(self):
        for fila in self.board:
            print(" | " .join(fila))

    def attack(self, opponent):
                board_impacts = []
                row_attack, col_attack = self.ask_row_col_attack()

                if row_attack < 0 or col_attack < 0 or row_attack >= len(self.attack_board) or col_attack >= len(self.attack_board[0]):
                    print("The position is not valid, less than 0 or out of bounds")
                    return 
                if self.attack_board[row_attack][col_attack] != " ":
                    print("You already attacked this position.")
                    return
                if opponent.board[row_attack][col_attack] in ["S", "D", "B"]:
                    print("Hit!")
                    self.attack_board[row_attack][col_attack] = "I"
                    opponent.board[row_attack][col_attack] = "I"
                    board_impacts.append((row_attack, col_attack))
                    print(f"Hit at {row_attack}, {col_attack}")

                    for ship in opponent.ships:
                        if ship.is_hit(row_attack, col_attack):
                            ship.hit()
                            print(f'This is hit {ship.hits} on {ship.__class__.__name__}')
                            if ship.hits == ship.size:
                                print(f"{ship.__class__.__name__} sunk!")

                else:
                    print("Water!")
                    self.attack_board[row_attack][col_attack] = "~"
                    

                print("\nOpponent's board updated:")
                for row in opponent.board:
                    print(" | ".join(row))

                print("\nYour attack board updated:")
                for row in self.attack_board:
                    print(" | ".join(row))

       

    def all_ships_sunk(self):
        
        """
    Continuously attacks the opponent until all of their ships are sunk.

    This function loops and performs attacks on the opponent by calling 
    `self.attack(opponent)` as long as there is at least one ship that 
    has not been fully hit (i.e., `ship.hits` is not equal to `ship.size`). 
    Once all ships are sunk, it prints a victory message.

    Parameters:
    opponent (Player): The opponent player object, expected to have a list of ships (`ships`),
                       each with `hits` and `size` attributes.

    Returns:
    None
    """
        
        while any(ship.hits != ship.size for ship in self.ships):
            return False    
        return True
    
    def get_user_input(self, prompt):
        user_input = input(prompt)
        if user_input == "exit":
            confirmation_input = input('Are you sure you want to exit? Confirm with: "YES", "yes", "y", "Y" ==> ')
            if confirmation_input.upper() in ["YES", "yes", "y", "Y"]:
                raise SystemExit("Player chose to exit the game")
        return user_input
    
    def ask_row_col_attack(self):
        while True:
            try:
                row_attack = int(self.get_user_input("Enter the row to attack: =>"))
                col_attack = int(self.get_user_input("Enter the column to attack: =>"))
                return row_attack, col_attack
            except ValueError as e:
                print('Error: Please enter an integer for the row and column.')
                print("Please try again.")
            except TypeError as e:
                print('Error: Invalid input type. Please enter integers.')
                print("Please try again.")

    def ask_start_row__start_col(self, name):
            start_row = None
            while start_row is None:
                try:
                    start_row = int(self.get_user_input(f"Enter the initial row of the {name}: =>"))
                except ValueError:
                    print('Error: Please enter an integer for the row.')
                    print("Please try again.")
                except TypeError:
                    print("Error: Please enter an integer for the row.")
                    print("Please try again!")

            start_col = None
            while start_col is None:
                try:
                    start_col = int(self.get_user_input(f"Enter the initial column of the {name}: =>"))
                except ValueError:
                    print('Error: Please enter an integer for the column.')
                    print("Please try again.")
                except TypeError:
                    print("Error: Please enter an integer for the column.")
                    print("Please try again!")

            while True:
                direction = self.get_user_input(f"Direction of the {name}: (H): Horizontal or (V): Vertical:").upper()
                if direction in ["H", "V"]:
                    return start_row, start_col, direction
                else:
                    print('Error: Invalid direction. Please enter "H" for Horizontal or "V" for Vertical.')
                    print("Please try again.")
# # Create player objects
# player = Player("Andres")
# print('*' * 40)
# print("Welcome to Battle Ship")
# print(f"The player's name is {player.name}")
# print('*' * 40)

# player.place_ships()

# print('*' * 40)
# print("After placing ships:")
# player.print_board()

# # Let's say there's an opponent player
# opponent = Player("Opponent")
# print('*' * 40)
# print("Welcome to Battle Ship")
# print(f"The second player's name is {opponent.name}")
# opponent.place_ships()

# print('*' * 40)
# print("After opponent placing ships:")
# opponent.print_board()

# # Start attacking phase
# print("Starts attacking player")
# player.attack(opponent)
# print("now attacking player")
# opponent.attack(player)