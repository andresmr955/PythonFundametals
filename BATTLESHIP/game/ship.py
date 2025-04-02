import sys

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, board, start_row, start_col, direction):
        
        self.start_row = start_row
        self.start_col = start_col
        self.direction = direction
        print(f'{self.start_row}, {self.start_col}, {self.direction.upper()}')
        
        if self.direction.upper() == "H":
            if self.start_col + self.size <= len(board[0]):
                
                can_place = True

                for i in range(self.size):
                    if board[self.start_row][self.start_col + i ] != " ":
                        print("You can not put your ship here")
                        can_place = False
                        break
                if can_place:
                        for i in range(self.size):
                            board[self.start_row][self.start_col + i ] = self.name
                            self.positions.append((self.start_row, self.start_col  + i))
                        print(f'The ships position is from ({self.start_row}, {self.start_col}) to ({self.start_row}, {self.start_col + self.size - 1})')
                        return True
            else: 
                print("The ship's size does not fit, please enter a correct size")
                sys.exit()
                return False 
                
          

        elif self.direction.upper() == "V": 
            if self.start_row + self.size <= len(board):
                can_place = True
                for i in range(self.size):
                    if board[self.start_row + i][self.start_col] != " ":
                        print("You can not put your ship here")
                        can_place = False
                        break
                if can_place:
                        for i in range(self.size):
                            board[self.start_row + i][self.start_col] = self.name
                            self.positions.append((self.start_row + i, self.start_col))
                        print(f'The ships position is ({self.start_row}, {self.start_col}) to ({self.start_row + self.size -1}, {self.start_col})')
                        return True
            else: 
                print("The ship's size does not fit, please enter a correct size")
                sys.exit()
                return False
        else:
            print("Invalid direction, please use (H) or (V)") 
            return False 
        
    def hit(self):
        self.hits += 1

        if self.hits == self.size:
            print(f'The {self.name} has been sunk')
            return True
        
        return False



class Destroyer(Ship): 
    def __init__(self):
        ##We have to call the constructor of parent class
        super().__init__("D", 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__("S", 3)
                
class Battleship(Ship):
    def __init__(self):
        super().__init__("B", 4)


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

'''
board = [
#       1      2     3     4    5
   A   [" " , " " , " " , " ", " "],
   B   [" " , " " , " " , " ", " "],
   C   [" " , " " , " " , " ", " "],
   D   [" " , " " , " " , " ", " "],
   E   [" " , " " , " " , " ", " "],
   F   [" " , " " , " " , " ", " "],
   G   [" " , " " , " " , " ", " "],
   H   [" " , " " , " " , " ", " "]
]
'''
##change hot fix

#board = [[ " " for _ in range(6) ] for _ in range(9) ]

#ship1 = Ship("S", 4)

