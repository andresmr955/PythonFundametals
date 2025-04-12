


board_opponent = [[" " for _ in range(3)] for _ in range(3)]


class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def set_position(self, row, col, board):
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    self.positions.append((row, col))
                else:
                    print(f"Error: La posición ({row}, {col}) ya está ocupada.")
            else:
                print(f"Error: La posición ({row}, {col}) está fuera del tablero.")

ship_ex = Ship("S", 2)
ship_ex.set_position(1,2, board_opponent)
ship_ex.set_position(1,1, board_opponent)

print("Board opponent")
for row in board_opponent:
    print(" | ".join(row))

board_user_impacts = [[" " for _ in range(3)] for _ in range(3)]
print("Board user impacts")
for row in board_user_impacts:
    print(" | ".join(row))


board_impacts = []

def attack():
    while ship_ex.hits != ship_ex.size:
    
        row_attack = int(input("Enter the row to attack: =>"))
        col_attack = int(input("Enter the column to attack: =>"))

        if row_attack < 0 or col_attack < 0 or row_attack >= len(board_opponent) or col_attack >= len(board_opponent[0]):
            print("The position is not valid, less than 0")
        else:
            if board_opponent[row_attack][col_attack] == " ":
                print("water!")

            else:
                print("Hint!") 
                board_impacts.append((row_attack, col_attack))
                print(board_impacts)
                board_user_impacts[row_attack][col_attack] = "I"
                board_opponent[row_attack][col_attack] = "I"
                ship_ex.hits += 1
                print(f'This is the hit {ship_ex.hits}')

        print("Board opponent updated")
        for row in board_opponent:
            print(" | ".join(row))

        print("Board user impacts updated")
        for row in board_user_impacts:
            print(" | ".join(row))
    print("The ship was sunk")
attack()
