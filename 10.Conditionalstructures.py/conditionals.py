##IF
x = 10
if x > 5:
    print("x es mayor que 5")
print("Afueras")
##ELSE

x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5")

##ELIF
x = 3
if x > 5:
    print("x es mayor que 5")
elif x == 5: 
    print("x es igual a 5")
else:
    print("x es menor o igual a 5")

#AND
x = 15
y = 20
if x > 10 and y > 25:
    print("X is greater than 10 and Y es menor que 25")
#OR
x = 15
y = 20

if x > 10 or y > 19:
    print("X is greater than 10 or Y es menor que 25")

#NOT
x = 20
if not x > 10:
    print("x is not greater than 10")


is_member = True
age = 15

if is_member: 
    if age>=15:
        print("You have access, cause you are older than 15")
    else:
        print("You have not access even though that you are memeber, cause you are not 15 years old")
else:
    print("You are not member")

#ROCK PAPER SICCORS
welcome = 'Welcome to the game rock, paper, siccors Rock(1), Paper(2), Scissors(3) '
print(welcome) 
UserOne = int(input('Please enter your choice: ')) 
userTwo = int(input('Please second player  enter your choice: '))
rock = 1
paper = 2
scissors = 3

if UserOne == paper and userTwo == rock:
    UserOne = 'paper'
    userTwo = 'rock'
    print(f'User one {UserOne} and user two {userTwo} User one won')
elif UserOne == rock and userTwo == scissors:   
    UserOne = 'rock'
    userTwo = 'scissors'
    print(f'User one rock and user two scissors User one won')  
elif UserOne == scissors and userTwo == paper: 
    UserOne = 'scissors'
    userTwo = 'paper'
    print(f'User one paper and user two rock User one won')  
else:
    print(f'User two userTwo and user one UserOne User two won')    