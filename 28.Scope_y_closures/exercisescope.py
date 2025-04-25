"""
crear 2 Funciones

La primera funcion recibira un diccionario que tenga 3 claves nam age and salary
La segunda funcion debera analizar el salario y  devolver el 
salario de los empleados que ganen cierto monto
"""


def receive_dic():
     
    return  [
    
    {
    "name" : "Carlos",
    "age" : "25", 
    "salary" : 4500
    }, 
    {
    "name" : "Camilo",
    "age" : "75", 
    "salary" : 8500
    },
    {
    "name" : "Sandra",
    "age" : "17", 
    "salary" : 3600
    }
]

def filtre_return(empleados, salary):
        return [empleado for empleado in empleados if empleado["salary"] >= salary]
        
create_empleados = receive_dic()

empleados_filtrados = filtre_return(create_empleados, 8500)

print(empleados_filtrados)