estudiantes = {
    "Juan": 85,
    "María": 92,
    "Pedro": 76,
    "Ana": 88,
    "Carlos": 95
}

#for (nombre, calificacion) in estudiantes.items():
   # print(nombre, calificacion)
cal_high = 0
cal_low = 100

for (nombre, calificacion) in estudiantes.items():
    
    if calificacion > cal_high:
        cal_high = calificacion
    
    if calificacion < cal_low:
        cal_low = calificacion
print(f'La calificacion mas alta es: {cal_high} y la calificacion mas baja es {cal_low}')

cal_alta = {nombre: calificacion for (nombre, calificacion) in estudiantes.items() if calificacion > 80}
print(cal_alta)