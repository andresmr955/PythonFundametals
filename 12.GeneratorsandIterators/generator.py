# We create a funcition

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

#Practice with generator

def devuelveTheFirstOterators(n): 
    num = 0
    while num < n:
        yield num 
        num +=2
gen = devuelveTheFirstOterators(10)
for num in gen:
    print(num)

comienza = 0
nNumberos = 10
while comienza <= nNumberos:
    
    print("Este es el comienza", comienza)
    
    if comienza % 2 == 0:
        comienza = comienza + 1
        print("Este es el comienza del if", comienza)