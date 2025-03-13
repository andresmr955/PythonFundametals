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