
def sumNumbers(x):
    result = 0
    if x <= 0:
        return "different from 0"
    else:
        for i in str(x):
            result+= int(i)    
        return result
number = int(input("number"))    

print(sumNumbers(number))