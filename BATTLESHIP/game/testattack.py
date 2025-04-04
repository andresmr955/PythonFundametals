row_attack = int(input("Enter the row to attack: =>"))
col_attack = int(input("Enter the column to attack: =>"))


board_opponent = [[" " for _ in range(3)] for _ in range(3)]

class Ship:
    def __init__(self):
        self.row = [1][2] = "X"
        self.col = [1][1] = "X"
        self.hints = 0

ship1 = Ship()
print(ship1.row)

print("Board opponent")
for row in board_opponent:
    print(" | ".join(row))

board_user_impacts = [[" " for _ in range(3)] for _ in range(3)]
print("Board user impacts")
for row in board_user_impacts:
    print(" | ".join(row))



board_impacts = []

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


print("Board opponent updated")
for row in board_opponent:
    print(" | ".join(row))

print("Board user impacts updated")
for row in board_user_impacts:
    print(" | ".join(row))