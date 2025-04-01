class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, board):
        self.board = board
        self.start_row = int(input("Ingresa la fila inicial: =>"))
        self.start_col = int(input("Ingresa la columna inicial: =>"))
        self.direction = input("Direction del varco: (H): Horinzontal o (V): Vertical: ")
        print(f'{self.start_row}, {self.start_col}, {self.direction.upper()}')
        
        if self.direction.upper() == "H":
            
            if self.start_col + self.size <= len(self.board[0]):
                
                can_place = True

                for i in range(self.size):
                    if self.board[self.start_row][self.start_col + i ] != " ":
                        print("You can not put your ship here")
                        can_place = False
                        break
                if can_place:
                        for i in range(self.size):
                            self.board[self.start_row][self.start_col + i ] = "S"
                            self.positions.append((self.start_row, self.start_col  + i))
                        print(f'The ships position is from ({self.start_row}, {self.start_col}) to ({self.start_row}, {self.start_col + self.size - 1}) )')
            else: 
                print("The ship's size is not good")
          

        elif self.direction.upper() == "V": 
            if  self.start_row + self.size <= len(self.board):
                can_place = True
                for i in range(self.size):
                    if self.board[self.start_row + i][self.start_col] != " ":
                        print("You can not put your ship here")
                        can_place = False
                        break
                if can_place:
                        for i in range(self.size):
                            self.board[self.start_row + i][self.start_col] = "S"
                            self.positions.append((self.start_row + i, self.start_col))
                            print(f'The ships position is ({self.start_row}, {self.start_col})')
            else: 
                print("The ship's size is not good")
        else:
            print("The customer does not want Horizontal")  
        
              

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

ship1 = Ship("El destructor", 3)
ship1.place_ship(board)


for fila in board:
    print(" | " .join(fila))

    