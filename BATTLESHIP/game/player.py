from ship import Destroyer, Submarine, Battleship


class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)]


    def place_ships(self):
        destroyer = Destroyer()
        submarine = Submarine()
        battleship = Battleship()

        while not destroyer.place_ship(self.board, start_row= int(input("Ingresa la fila inicial del destroyer: =>")), 
                                start_col= int(input("Ingresa la columna inicial del destroyer: =>")), 
                                direction= input("Direction del destroyer: (H): Horinzontal o (V): Vertical: ")):
            
            print("Try again for the Destroyer.")
        while not submarine.place_ship(self.board, start_row= int(input("Ingresa la fila inicial del submarino: =>")), 
                             start_col= int(input("Ingresa la columna inicial del submarino: =>")), 
                             direction= input("Direction del submarino: (H): Horinzontal o (V): Vertical: ")):
            
            print("Try again for the submarine.")

        while not battleship.place_ship(self.board, start_row= int(input("Ingresa la fila inicial del battleship: =>")), 
                              start_col= int(input("Ingresa la columna inicial del battleship: =>")), 
                              direction= input("Direction del battleship: (H): Horinzontal o (V): Vertical: ")):
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
