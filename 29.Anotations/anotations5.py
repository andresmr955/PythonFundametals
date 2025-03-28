from typing import Union

##With optional we are saying that the function can return an integer or None
def find_employee(salary: Union[int, float]) -> float:
    """
    Process a salary that it can be integer or float and return as a float

    Parameters:
    Salary (Union[int, float]): A salary that it can be an integer or float

    return:
    float: The salary converted a float
    
    """
    