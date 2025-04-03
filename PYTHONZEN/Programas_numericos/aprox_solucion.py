from time import time
objective = 25
epsilon = 0.1
paso = epsilon**2
answer = 0.0
started_time = time()

while abs(answer**2 - objective) >= epsilon and answer <= objective:
    print(abs(answer**2 - objective), answer)
    answer += paso

total_time = time() - started_time

if abs(answer**2 - objective) >= epsilon:
    print(f'Does not have an integer square root')
    print(f'It took {total_time} seconds')
else:
    print(f'The square root of {objective} is {answer}')
    print(f'It took {total_time} seconds')