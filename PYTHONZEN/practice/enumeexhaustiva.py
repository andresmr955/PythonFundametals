num_user = int(input("Give me a number: => "))
answer = 0

while answer**2 < num_user:
    answer += 1  
    
if answer**2 == num_user:
    print(f'The square root of {num_user} is {answer}')
else:
    print(f'The given number {num_user} has not square root')
    
    a = {1,2}
