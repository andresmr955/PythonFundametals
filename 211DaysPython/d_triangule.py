def triangle(size, character):
    triangle=""
    for i in range(size):
        spaces = ' ' * (size - i - 1)
        character_v = character * ( 2 * i + 1)
            
        solution = spaces + character_v + spaces

        if i < size -1:
            solution+= "\n"

        triangle+= solution
    return triangle

print(triangle(6, "$") )