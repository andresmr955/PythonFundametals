from typing import Optional

##With optional we are saying that the function can return an integer or None
def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Search an employee's ID inside a list from IDS and return the value if it exists 

    Parameters: 
    employee_ids (list[int]): List of IDs of employees
    employee_id (int): ID to search

    """

    if employee_id in employee_ids:
        return employee_id
    return None