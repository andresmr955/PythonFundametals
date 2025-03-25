try:
    divisor = int(input("Enter a number divisor: "))
    result = 100/divisor
except ZeroDivisionError as e:
    print("Error, the divisor can not be zero ")
    print("It occurred an error: ", e)
except ValueError as e:
    print("Please enter a number, nor other value")
    print("It occurred an error: ", e)



#--------------------------------------------------------------------------

def print_exception_hierarchy(exception_class, indent= 0):
    print(' ' *  indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)
print_exception_hierarchy(Exception)

##It is a good practice name the name of the exception