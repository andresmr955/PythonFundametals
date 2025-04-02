import sys

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, board):
        
        self.start_row = int(input("Ingresa la fila inicial: =>"))
        self.start_col = int(input("Ingresa la columna inicial: =>"))
        self.direction = input("Direction del varco: (H): Horinzontal o (V): Vertical: ")
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
                        print(f'The ships position is from ({self.start_row}, {self.start_col}) to ({self.start_row}, {self.start_col + self.size - 1}) )')
            else: 
                print("The ship's size does not fit, please enter a correct size")
                sys.exit()
                return False 
                
          

        elif self.direction.upper() == "V": 
            if  self.start_row + self.size <= len(board):
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
                            print(f'The ships position is ({self.start_row}, {self.start_col})')
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
        super().__init__("Destroyer", 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", 3)
                
class Battleship(Ship):
    def __init__(self):
        super().__init__("BattleShip", 4)

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


board = [[ " " for _ in range(5) ] for _ in range(8) ]

ship1 = Ship("S", 4)
ship1.place_ship(board)

ship1.hit()
for fila in board:
    print(" | " .join(fila))

    