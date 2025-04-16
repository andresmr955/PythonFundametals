from ship import Destroyer, Submarine, Battleship


class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.attack_board = [[" " for _ in range(10)] for _ in range(10)]

    def place_ships(self):
        destroyer = Destroyer()
        submarine = Submarine()
        battleship = Battleship()

    
        while not destroyer.place_ship(self.board, start_row= int(input("Enter the initial row of the destroyer: =>")), 
                            start_col = int(input("Enter the initial column of the destroyer: =>")), 
                            direction = input("Direction of the destroyer: (H): Horizontal or (V): Vertical:")):     
            print("Try again for the Destroyer.")
        self.ships.append(destroyer)
            
        while not submarine.place_ship(self.board, start_row= int(input("Enter the initial row of the submarine: =>")), 
                            start_col = int(input("Enter the initial column of the submarine: =>")), 
                            direction = input("Submarine direction: (H): Horizontal or (V): Vertical: ")):
            
            print("Try again for the submarine.")
        self.ships.append(submarine)

        while not battleship.place_ship(self.board, start_row= int(input("Enter the starting row of the battleship: =>")), 
                            start_col = int(input("Enter the initial column of the battleship: =>")), 
                            direction = input("Direction of the battleship: (H): Horizontal or (V): Vertical: ")):
            print("Try again for the battleship.")
        self.ships.append(battleship)
        
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

       

    def all_ships_sunk(self, opponent):
        
        while any(ship.hits != ship.size for ship in opponent.ships):
            self.attack(opponent) 

        print("All enemy ships have been sunk!")
        return True
# Create player objects
player = Player("Andres")
print('*' * 40)
print("Welcome to Battle Ship")
print(f"The player's name is {player.name}")
print('*' * 40)

player.place_ships()

print('*' * 40)
print("After placing ships:")
player.print_board()

# Let's say there's an opponent player
opponent = Player("Opponent")
print('*' * 40)
print("Welcome to Battle Ship")
print(f"The second player's name is {opponent.name}")
opponent.place_ships()

print('*' * 40)
print("After opponent placing ships:")
opponent.print_board()

# Start attacking phase
print("Starts attacking player")
player.attack(opponent)
print("now attacking player")
opponent.attack(player)