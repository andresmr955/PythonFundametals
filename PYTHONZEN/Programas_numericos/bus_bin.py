objective = 25
epsilon = 0.01
down = 0.0
high = max(1.0, objective)
answer = (high + down) / 2 

while abs(answer**2 - objective) >= epsilon:
    print(answer, down, high)
    if answer**2 < objective:
        down = answer
    else:
        high = answer
    answer = (high + down) / 2
print(answer)