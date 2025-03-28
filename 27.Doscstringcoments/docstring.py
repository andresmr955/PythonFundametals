def calculate_average(numbers):
    """
    Calculates the average from a number list

    Parameter:
    numbers (list): List's numbers integers or floats
    
    Return:
    float: The average of the numbers in a list
    """

    return sum(numbers) / len(numbers)

#Printing the result of the function
print(calculate_average([1, 2, 3, 4, 5, 6, 7, 8]))