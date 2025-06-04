empleados = [
    "Ana Torres",
    "Luis Ramírez",
    "María Gómez",
    "Carlos Díaz",
    "Laura Pérez",
    "José Herrera",
    "Paula Ríos",
    "Diego Castro",
    "Sofía Medina",
    "Ricardo Molina"
]


def add_employees(employee):
    new_list = []
    new_list.append(employee)

    return new_list

def delete_employees(list: list, employee: str) -> list:
    new_list = []
    for emplo in list:
        if emplo != employee:
            new_list.append(emplo)
    return new_list            

if __name__ == "__main__":
    result = delete_employees(empleados,"Diego Castro")
    print(result)