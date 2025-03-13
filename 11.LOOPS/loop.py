numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Here is equal to: ", i+1)
for i in range(3,10):
    print(i)

fruits = ["Apple", "Pear", "Grape", "Orange","Tomato"]
for fruit in fruits:
    print(fruit)
    if fruit == "Orange":
        print("Orange found it")


#WHILE 
x = 0
while x<=5:
    
    print(x)
    x +=1  #x = x +1

#BREAK    
x = 0
while x<5:
    if x ==3:
        break
    print(x)
    x +=1  #x = x +1 
#Skip
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i == 3:
        continue
    print("Here i is equal to: ", i)

#FIBONACCI SERIE

x,y = 0,1
while y < 1000:
    print("This is the order: => ", y)
    x,y = y, x+y

x = int(input("Please enter an integer"))
if x < 0:
    x = 0
    print('Negative changed to zero')    
elif x == 0:
    print('Negative changed to zero')
elif x == 1:
    print('Single')
else: 
    print('More')

##FOR STATEMENTS

words = ['cat', 'window']