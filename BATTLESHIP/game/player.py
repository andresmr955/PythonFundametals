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
            while not ship.place_ship(self.board, start_row= int(input(f"Enter the initial row of the {name}: =>")), 
                                start_col = int(input(f"Enter the initial column of the {name}: =>")), 
                                direction = input(f"Direction of the {name}: (H): Horizontal or (V): Vertical:")):     
                print("Try again for the Destroyer.")
            self.ships.append(ship)
            
    def print_board(self):
        for fila in self.board:
            print(" | " .join(fila))

    def attack(self, opponent):
                board_impacts = []
                row_attack = int(input("Enter the row to attack: =>"))
                col_attack = int(input("Enter the column to attack: =>"))

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