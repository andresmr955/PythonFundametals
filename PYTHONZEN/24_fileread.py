import os

root_absolute = os.path.abspath('text.txt')
print(root_absolute)

file = open('./text.txt')
#print(file.read())

## second option 
print(file.readline())
print(file.readline())
#print(file.read())
print(file.readline())



# we can use for to iterate
for line in file:
    print(line)

## the right sintaxys to open and close
with open('filename' )as file:
    for line in file:
        print(line)

# We liberate the pc's memory
file.close()