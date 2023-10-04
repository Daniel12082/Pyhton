from datetime import datetime,date
'''fecha = input("Ingrese la fecha en formato(dd-mm-yyyy)").striptime()
fecha = datetime
print(fecha)
"""print(fecha)
print(type(fecha.strftime("")))
if fecha > date.today():
    print("OKKK")
elif fecha < datetime.today():
    print("NOOO")"""
print(date.today())'''

"""hora = datetime.now().time()
print(type(hora))
print(hora)"""
nombre_paciente = input("Nombre del paciente: ")
bandera_fecha = True
while bandera_fecha == True:
    fecha_Str= input("Ingrese la fecha de la cita(aaaa-mm-dd): ")
    try:
        fecha_cita = datetime.strptime(fecha_Str, '%Y-%m-%d').date()
        fecha_actual = date.today()
        if fecha_cita> fecha_actual:
            break
        else:
            print("Fecha de la cita debe ser mayor a la fecha actual")
    except ValueError:
            print("Formato de fecha incorrecto intene nuevamente")
bandera_hora = True  
while bandera_hora == True:
    hora_str=input("Ingrese la hora de la cita 24H (hh:mm): ")
    try:
        hora_cita = datetime.strptime(hora_str, '%H:%M').time()
        break
    except ValueError:
        print("Formato de hora incorrecto intene nuevamente")
print((fecha_Str))
print(type(hora_str))
