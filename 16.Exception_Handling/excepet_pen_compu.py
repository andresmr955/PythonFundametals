def divide_elements_of_list(list, divisor):
    try:
        if divisor == 0:
        
            return [i / divisor for i in list]
    except ZeroDivisionError as e:
        
        print("Error, the divisor can not be zero")
        print("It occurred an error: ", e)
        return list
    except TypeError as e:
        print("Please enter a number, nor other value")
        print("It occurred an error: ", e)
list = list(range(10))
divisor = 0

print(divide_elements_of_list(list, divisor))