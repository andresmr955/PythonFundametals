from typing import Optional

def find_employee_int(id1: int, id2: int) -> int:
        if type(id1) and type(id2) == int:
            return id1 + id2
        return id1 + id2
print(find_employee_int(4,8))

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