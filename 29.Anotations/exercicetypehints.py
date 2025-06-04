from typing import Union, Optional

test_ex = [
    {'name': 'Alice', 'age': 30, 'salary': 60000},
    {'name': 'Bob', 'age': 25, 'salary': 55000},
    {'name': 'Charlie', 'age': 35, 'salary': 70000},
    {'name': 'David', 'age': 28, 'salary': 62000},
    {'name': 'Eve', 'age': 32, 'salary': 68000},
    {'name': 'Frank', 'age': 27, 'salary': 58000},
    {'name': 'Grace', 'age': 31, 'salary': 65000},
    {'name': 'Henry', 'age': 29, 'salary': 59000},
    {'name': 'Ivy', 'age': 33, 'salary': 72000},
    {'name': 'Jack', 'age': 26, 'salary': 56000}
]

salary_limit = 70000

def process_list_dic_type_hints(list_para: list, salary: Union[float, int ]) -> Optional[list]:
    return [employee for employee in list_para if employee['salary'] >= salary]

print(process_list_dic_type_hints(test_ex, salary_limit))

def filter_func(list_para: list, salary: Union[int, float]) -> Optional[list]:
    return list(filter(lambda employee: employee['salary'] >= salary, list_para))

print(filter_func(test_ex, salary_limit))

def map_func(list_para: list, salary: Union[int, float]) -> Optional[list]:
    return list(map(lambda employee: employee if employee['salary'] >= salary else None , list_para))

print(map_func(test_ex, salary_limit))