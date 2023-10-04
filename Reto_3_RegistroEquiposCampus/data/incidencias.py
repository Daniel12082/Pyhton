import core
import os
from datetime import datetime

diccIncidencias = {"data": []}
diccEquipos = {"data": []}

def LoadInfoIncidencias():
    global diccEquipos
    global diccIncidencias
    if core.checkFile("incidencias.json"):
        diccIncidencias = core.LoadInfo("incidencias.json")
    else:
        core.crearInfo("incidencias.json", diccIncidencias)

def RegIncidencias():
    global diccEquipos
    global diccIncidencias
    
    if core.checkFile("equipos.json"):
        diccEquipos = core.LoadInfo("equipos.json")
    else:
        core.crearInfo("equipos.json", diccEquipos)
    
    reg = True
    while reg:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^18}{}{:^17}|".format(' ', 'GESTION DE INCIDENCIAS', ' '))
        print('+','-'*55,'+')
        print("1. Agregar incidencias")
        print("2. Lista de incidencias")
        print("3. Volver al menú principal\n")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            #SELECCION DE AREA
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^20}{}{:^20}|".format(' ', 'SELECCION DE AREA', ' '))
            print('+','-'*55,'+')
            print("1. Area de Training\n2. Area de Review")
            area = int(input("Selecciona una opción: "))
            #SELECCION DE LUGAR
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^19}{}{:^20}|".format(' ', 'SELECCION DE LUGAR', ' '))
            print('+','-'*55,'+') 
            if area == 1:
                area = "Training"
                print("1. Apolo\n2. Artemis\n3. Sputnik\n4. Skylab")
                lugar = int(input("Selecciona una opción: "))
                if lugar == 1:
                    lugar = "Apolo"
                elif lugar == 2:
                    lugar = "Artemis"
                elif lugar == 3:
                    lugar = "Sputnik"
            if area == 2:
                area = "Review"
                print("1. Corvus\n2. Endor")
                lugar = int(input("Selecciona una opción: "))
                if lugar == 1:
                    lugar = "Corvus"
                elif lugar == 2:
                    lugar = "Endor"
            #SELECCION DE CATEGORIA DE INCIDENCIA
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^12}{}{:^12}|".format(' ', 'SELECCION DE NIVEL DE CATEGORIA', ' '))
            print('+','-'*55,'+') 
            print("1. Hardware\n2. Sotware")
            categorias = int(input("Selecciona una opción: "))
            if categorias == 1:
                categorias = "Hardware"
            elif categorias == 2:
                categorias = "Software"
            #SELECCION DE NIVEL DE INCIDENCIA
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^12}{}{:^12}|".format(' ', 'SELECCION DE NIVEL DE INCIDENCIAS', ' '))
            print('+','-'*55,'+') 
            print("1. Leve\n2. Moderada\n3. Critica")
            incidencia = int(input("Selecciona una opción: "))
            if incidencia == 1:
                incidencia = "Leve"
            elif incidencia == 2:
                incidencia = "Moderada"
            elif incidencia == 3:
                incidencia = "Critica"
            #SELECCION DE EQUIPO
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^18}{}{:^17}|".format(' ', 'ID DE EQUIPOS REGISTRADOS', ' '))
            print('+','-'*55,'+')
            if core.checkFile("equipos.json"):
                diccEquipos = core.LoadInfo("equipos.json")
            else:
                core.crearInfo("equipos.json", diccEquipos)
            idpc=0
            computador=True
            while computador:
                for i in diccEquipos["data"]:
                    if i["area"]["area"] == area and i["area"]["lugar"]["lugar"] == lugar:
                        print(i["area"]["lugar"]["idPc"])
                        id = input("Ingres el codigo del pc que desaea registra la incidencia: ")
                        if id == i["area"]["lugar"]["idPc"]:
                            idpc= {
                                "idPc": i["area"]["lugar"]["idPc"],
                                "idAu": i["area"]["lugar"]["idAu"],
                                "idT": i["area"]["lugar"]["idT"],
                                "idM": i["area"]["lugar"]["idM"],
                                "idMo": i["area"]["lugar"]["idMo"]
                            }
                            computador=False
                            break
                if idpc == 0:
                    print("No se encontró el código del PC.")
                    computador=False
            #Fecha
            fecha = datetime.now()
            fecha_formateada = fecha.strftime("%d/%m/%Y")
            #SELECCION DE TRAINER
            if core.checkFile("trainer.json"):
                diccTrainer = core.LoadInfo("trainer.json")
            else:
                core.crearInfo("trainer.json", diccTrainer)
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^18}{}{:^17}|".format(' ', 'ID DE TRAINERS REGISTRADOS', ' '))
            print('+','-'*55,'+')
            for i in diccTrainer["data"]:
                print(f'NOMBRE TRAINER: {i["nombre"]} ID: {i["id"]}')
            trainer_id = input("Ingrese el ID del trainer que esta ingresando la incidencia: ")
            for i in diccTrainer["data"]:
                if i["id"] == trainer_id:
                    trainer_info = {
                        "idTrainer": i["id"],
                        "nombre": i["nombre"],
                    }
                    break
            #DESCRIPCION DE LA INCIDENCIA
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^18}{}{:^17}|".format(' ', 'NOMBRE DE LA INCIDENCIA', ' '))
            print('+','-'*55,'+')
            incidencia=input("Explique cual es la incidencia: ")
            data = {
                "id": str(len(diccIncidencias['data']) + 1).zfill(4),
                "area": {
                    "area": area,
                    "lugar": {
                        "fecha" : fecha_formateada,
                        "categoria": categorias,
                        "lugar": lugar,
                        "incidencia": incidencia,
                        "idPc": idpc,
                        "idTrainer" : trainer_info,
                        "incidencia": incidencia
                    }
                }
            }
            diccIncidencias['data'].append(data)
            core.crearInfo("incidencias.json", data)
            
        if opcion == 2:
            os.system("clear")
            Insidencias = core.LoadInfo("incidencias.json")
            print('+','-'*55,'+')
            for i in Insidencias["data"]:
                print(f'|{" ":^27}ID {i["id"]}{" ":^26}|')
                print('+','-'*55,'+')
                print(f'Fecha: {i["area"]["lugar"]["fecha"]}\nArea: {i["area"]["area"]} \nLugar: {i["area"]["lugar"]["lugar"]} \nCategoria: {i["area"]["lugar"]["categoria"]}\nIncidencia: {i["area"]["lugar"]["incidencia"]}')
                print('+','-'*55,'+')
            input("Presiona enter para continuar .....")
        if opcion == 3:
            reg = False
