def divide_elements_of_list(list, divisor):
    try:
        return [i / divisor for i in list]
    except ZeroDivisionError as e:
        
        print("Error, the divisor can not be zero")
        print("It occurred an error: ", e)
        return list
    except TypeError as e:
        print("Please enter a number, nor other value")
        print("It occurred an error: ", e)
        return e
list = list(range(10))
divisor = "k"

print(divide_elements_of_list(list, divisor))