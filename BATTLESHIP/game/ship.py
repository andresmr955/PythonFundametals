class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, board, start_row, start_col, direction):
        self.board = board
        self.start_row = start_row
        self.start_col = start_col
        self.direction = direction

            
        board[2][1] =  "S"     ''' start_row '''
        board[2][2] =  "S"  
        board[2][3] =  "S"   ''' start_col '''
        direction = "right"


ship1 = Ship("El destructor", 2)


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


board = [
#       1      2     3     4    5
    [" " , " " , " " , " ", " "],
    [" " , " " , " " , " ", " "],
    [" " , " " , " " , " ", " "],
    [" " , " " , " " , " ", " "],
    [" " , " " , " " , " ", " "],
    [" " , " " , " " , " ", " "],
    [" " , " " , " " , " ", " "],
    [" " , " " , " " , " ", " "]
]


#Estos estan en la columna 2 en la posicion a, b y c      
board[0][1] = 'S' 
board[1][1] = 'S'
board[2][1] = 'S'


for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=" ")
        if board[i][j] == ' ':
             board[i][j] == 'S'
    print()	


#for fila in board:
   # print(fila)

    