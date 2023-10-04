import os
import core
from datetime import datetime,date
diccCitas={"data":[]}

def LoadInfoCitas():
    global diccCitas
    if (core.checkFile("citas.json")):
        diccCitas = core.LoadInfo("citas.json")
    else:
        core.crearInfo("citas.json",diccCitas)

def pedir_cita_medica():
    os.system("clear")
    nombre_paciente = input("Ingrese el nombre del paciente: ".upper())
    
    while True:
        fecha_str = input("Ingrese la fecha de la cita (formato dd/mm/aaaa): ")
        try:
            fecha_cita = datetime.strptime(fecha_str, "%d/%m/%Y").date()
            fecha_actual = date.today()
            if fecha_cita > fecha_actual:
                break
            else:
                print("Error: La fecha de la cita debe ser mayor que la fecha actual. Intente nuevamente.")
        except ValueError:
            print("Error: La fecha no tiene el formato correcto. Intente nuevamente.")
    
    while True:
        hora_str = input("Ingrese la hora de la cita (formato hh:mm): ")
        try:
            hora_cita = datetime.strptime(hora_str, "%H:%M")
            break
        except ValueError:
            print("Error: La hora no tiene el formato correcto. Intente nuevamente.")

    motivo_consulta = input("Ingrese el motivo de la consulta: ")

    data = {
        "nombre_paciente": nombre_paciente,
        "fecha_cita": fecha_cita.strftime("%d/%m/%Y"),
        "hora_cita": hora_cita.strftime("%H:%M"),
        "motivo_consulta": motivo_consulta
    }
    diccCitas["data"].append(data)
    core.crearInfo("citas.json",data)

def buscar_cita():
    criterio_busqueda = input("Ingrese el criterio de búsqueda (nombre del paciente o fecha de la cita): ")
    citas_encontradas = []

    for cita in diccCitas["data"]:
        if criterio_busqueda.upper() in cita["nombre_paciente"]or criterio_busqueda == cita["fecha_cita"]:
            citas_encontradas.append(cita)

    if citas_encontradas:
        print("Citas encontradas:")
        for i, cita in enumerate(citas_encontradas, 1):
            print(f"{i}. Nombre del paciente:", cita["nombre_paciente"])
            print("   Fecha de la cita:", cita["fecha_cita"])
            print("   Hora de la cita:", cita["hora_cita"])
            print("   Motivo de la consulta:", cita["motivo_consulta"])
            print("-" * 60)
    else:
        print("No se encontraron citas con el criterio de búsqueda.")

def cancelar_cita():
    criterio_busqueda = input("Ingrese el criterio de búsqueda (nombre del paciente o fecha de la cita): ")
    citas_encontradas = []

    for cita in diccCitas["data"]:
        if criterio_busqueda.lower() in cita["nombre_paciente"].lower() or criterio_busqueda == cita["fecha_cita"]:
            citas_encontradas.append(cita)

    if citas_encontradas:
        print("Citas encontradas:")
        for i, cita in enumerate(citas_encontradas, 1):
            print(f"{i}. Nombre del paciente:", cita["nombre_paciente"])
            print("   Fecha de la cita:", cita["fecha_cita"])
            print("   Hora de la cita:", cita["hora_cita"])
            print("   Motivo de la consulta:", cita["motivo_consulta"])
            print("-" * 60)

        indice_cancelar = int(input("Ingrese el número de la cita que desea cancelar: ")) - 1

        if indice_cancelar >= 0 and indice_cancelar < len(citas_encontradas):
            cita_cancelar = citas_encontradas[indice_cancelar]
            print(f"Se ha cancelado la cita de {cita_cancelar['nombre_paciente']}")

            diccCitas["data"].remove(cita_cancelar)
            core.crearInfo("citas.json",diccCitas)