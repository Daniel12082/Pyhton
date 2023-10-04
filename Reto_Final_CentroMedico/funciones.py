import core
import os
from datetime import datetime,date
diccCitas = {"data":[]}
def  LoadInfoCitas():
    global diccCitas
    if (core.checkFile("citas.json")):
        diccCitas = core.loadInfo("citas.json")
    else:
        core.crearInfo("citas.json",diccCitas)


def agregarCita():
    os.system("clear")
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
                os.system('clear')
        except ValueError:
                print("Formato de fecha incorrecto intene nuevamente")
                os.system('clear')
    bandera_hora = True  
    while bandera_hora == True:
        hora_str=input("Ingrese la hora de la cita 24H (hh:mm): ")
        try:
            hora_cita = datetime.strptime(hora_str, '%H:%M').time()
            break
        except ValueError:
            print("Formato de hora incorrecto intene nuevamente")
            os.system('clear')
    motivo=input("Motivo de la cita: ")
    data={
        "nombre_paciente":nombre_paciente.upper(),
        "fecha_cita":fecha_Str,
        "hora_cita":hora_str,
        "motivo":motivo.upper(),
    }
    diccCitas["data"].append(data)
    core.crearInfo("citas.json",data)

def buscarCita():
    os.system("clear")
    search = True
    while search== True:
        try:
            opcion = 0
            opcion=int(input("1.Buscar por nombre\n2.Buscar por fecha\nSeleccion una opcion: "))
            pacientes={"datos":[]}
            if opcion == 1:
                nombre_paciente = input("Nombre del paciente: ")
                for i,item in enumerate(diccCitas["data"]):
                    if nombre_paciente.upper() in (item["nombre_paciente"]):
                        pacientes["datos"].append(item)
            print("-"*50)
            if opcion == 2:
                bandera_fecha = True
                while bandera_fecha == True:
                    fecha_Str= input("Ingrese la fecha de la cita(aaaa-mm-dd): ")
                    try:
                        fecha_cita = datetime.strptime(fecha_Str, '%Y-%m-%d').date()
                        fecha_actual = date.today()
                        if fecha_cita> fecha_actual:
                            break
                        else:
                            os.system('clear')
                            print("Fecha de la cita debe ser mayor a la fecha actual")
                    except ValueError:
                            os.system('clear')
                            print("Formato de fecha incorrecto intene nuevamente")
                for i,item in enumerate(diccCitas["data"]):
                    if fecha_Str in (item["fecha_cita"]):
                        pacientes["datos"].append(item)
            print("-"*50)
            for i,item in enumerate(pacientes["datos"]):
                print(f"{i+1}.Nombre:{item['nombre_paciente']}\nFecha:{item['fecha_cita']}\nHora:{item['hora_cita']}")
            input("presiones enter para continuar")
            break
        except ValueError:
            print("Seleccione una opcion valida")
            input("presione enter para continuar")
            os.system('clear')

def modificarCita():
    search = True
    while search== True:
        try:
            
            os.system('clear')
            print("DATOS DE LA CITA ORIGINAL")
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
                        os.system('clear')
                        print("Fecha de la cita debe ser mayor a la fecha actual")
                except ValueError:
                        os.system('clear')
                        print("Formato de fecha incorrecto intene nuevamente")
            for i,item in enumerate(diccCitas["data"]):
                if fecha_Str in (item["fecha_cita"]) or nombre_paciente in (item["nombre_paciente"]):
                    os.system('clear')
                    print("NUEVOS DATOS PARA LA CITA")
                    nombre_paciente = input("Ingrese el nuevo nombre o enter para continuar: ").upper()or item["nombre_paciente"]
                    modificar =bool(input("Desea modificar la fecha s(Si) enter (no): "))
                    if modificar == True:
                        bandera_fecha = True
                        while bandera_fecha == True:
                            fecha_nueva= input("Ingrese la fecha de la cita(aaaa-mm-dd): ")
                            try:
                                fecha_cita = datetime.strptime(fecha_nueva, '%Y-%m-%d').date()
                                fecha_actual = date.today()
                                if fecha_cita> fecha_actual:
                                    break
                                else:
                                    print("Fecha de la cita debe ser mayor a la fecha actual")
                                    os.system('clear')
                            except ValueError:
                                    print("Formato de fecha incorrecto intene nuevamente")
                                    os.system('clear')
                    if modificar == False:
                        fecha_nueva = item["fecha_cita"]
                    fecha_cita = fecha_nueva
                    modificar_hora =bool(input("Desea modificar la hora s(Si) enter (no): "))
                    if modificar_hora == True:
                        bandera_hora = True  
                        while bandera_hora == True:
                            hora_str=input("Ingrese la hora de la cita 24H (hh:mm): ")
                            try:
                                hora_cita = datetime.strptime(hora_str, '%H:%M').time()
                                break
                            except ValueError:
                                print("Formato de hora incorrecto intene nuevamente")
                                os.system('clear')
                    if modificar_hora == False:
                        hora_str = item["hora_cita"]
                    hora_cita = hora_str
                    motivo = input("Ingrese el nuevo motivo o enter para no modificar: ").upper() or item["motivo"]
                    data = {
                        "Nombre_paciente":nombre_paciente,
                        "fecha_cita":fecha_cita,
                        "hora_cita":hora_cita,
                        "motivo":motivo,
                    }
                    core.editInfo("citas.json",data)
                    break
                else:
                    print("No se encontro la cita")
                    search = bool(input(
                        "Ingrese s(seguir buscando) enter (para salir): "))
        except ValueError:
            print("Seleccione una opcion valida")
            input("presione enter para continuar")
            os.system('clear')

def cancelarCita():
    os.system("clear")
    search = True
    while search== True:
        try:
            opcion = 0
            opcion=int(input("1.Buscar por nombre\n2.Buscar por fecha\nSeleccion una opcion: "))
            pacientes=[]
            if opcion == 1:
                nombre_paciente = input("Nombre del paciente: ")
                for i,item in enumerate(diccCitas["data"]):
                    if nombre_paciente.upper() in (item["nombre_paciente"]):
                        pacientes.append(item)
            print("-"*50)
            if opcion == 2:
                bandera_fecha = True
                while bandera_fecha == True:
                    fecha_Str= input("Ingrese la fecha de la cita(aaaa-mm-dd): ")
                    try:
                        fecha_cita = datetime.strptime(fecha_Str, '%Y-%m-%d').date()
                        fecha_actual = date.today()
                        if fecha_cita> fecha_actual:
                            break
                        else:
                            os.system('clear')
                            print("Fecha de la cita debe ser mayor a la fecha actual")
                    except ValueError:
                            os.system('clear')
                            print("Formato de fecha incorrecto intene nuevamente")
                for i,item in enumerate(diccCitas["data"]):
                    if fecha_Str in (item["fecha_cita"]):
                        pacientes.append(item)
            if pacientes:
                print("Citas encontradas:")
                for i, cita in enumerate(pacientes, 1):
                    print(f"{i}. Nombre del paciente:", cita["nombre_paciente"])
                    print("   Fecha de la cita:", cita["fecha_cita"])
                    print("   Hora de la cita:", cita["hora_cita"])
                    print("   Motivo de la consulta:", cita["motivo"])
                    print("-" * 60)

                indice_cancelar = int(input("Ingre el numero de la cita que desea cancelar: "))-1

                if indice_cancelar >=0 and indice_cancelar < len(pacientes):
                    cita_cancelar = pacientes[indice_cancelar]
                    print(f"Se ha cancelado la cita de {cita_cancelar['nombre_paciente']}")
                    diccCitas ["data"].remove(cita_cancelar)
                    core.editInfo("citas.json",diccCitas)
            break
        except ValueError:
            print("Seleccione una opcion valida")
            input("presione enter para continuar")
            os.system('clear')
    