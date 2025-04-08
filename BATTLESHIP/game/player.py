from ship import Destroyer, Submarine, Battleship


class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)]
        self.ships = []

    def place_ships(self):
        destroyer = Destroyer()
        submarine = Submarine()
        battleship = Battleship()

        

    
        while not destroyer.place_ship(self.board, start_row= int(input("Enter the initial row of the destroyer: =>")), 
                            start_col = int(input("Enter the initial column of the destroyer: =>")), 
                            direction = input("Direction of the destroyer: (H): Horizontal or (V): Vertical:")):     
            print("Try again for the Destroyer.")
            
        while not submarine.place_ship(self.board, start_row= int(input("Enter the initial row of the submarine: =>")), 
                            start_col = int(input("Enter the initial column of the submarine: =>")), 
                            direction = input("Submarine direction: (H): Horizontal or (V): Vertical: ")):
            
            print("Try again for the submarine.")

        while not battleship.place_ship(self.board, start_row= int(input("Enter the starting row of the battleship: =>")), 
                            start_col = int(input("Enter the initial column of the battleship: =>")), 
                            direction = input("Direction of the battleship: (H): Horizontal or (V): Vertical: ")):
            print("Try again for the battleship.")
        
    def print_board(self):
        for fila in self.board:
            print(" | " .join(fila))

            

player = Player("Andres")
print('*' * 40)
print("Welcome to Battle Ship")
print(f"The players name is {player.name}")
print('*' * 40)

player.place_ships()


print('*' * 40)
print("After placing ships:")
player.print_board()
