


def factorial(num):
    '''
        This function takes a number and returns the factorial of that number

        n int > 
    
        return n!    
       '''
    print(num)
    if num == 1:
        return 1
    
    return num * factorial(num - 1)




num_given = int(input('Enter a number to calculate its factorial: ')) 
print(factorial(num_given))

num_given = int(input('Enter a number to calculate its factorial: ')) 
print(factorial(num_given))
