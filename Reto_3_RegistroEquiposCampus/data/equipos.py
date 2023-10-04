import core
import os

diccEquipos = {"data": []}

def LoadInfoEquipos():
    global diccEquipos
    if core.checkFile("equipos.json"):
        diccEquipos = core.LoadInfo("equipos.json")
    else:
        core.crearInfo("equipos.json", diccEquipos)

def RegEquipos():
    os.system("clear")
    print('+','~'*55,'+')
    print("|{:^21}{}{:^21}|".format(' ', 'REGISTRO EQUIPO', ' '))
    print('+','~'*55,'+')
    id = str(len(diccEquipos["data"]) + 1).zfill(4)
    print(f"El id de su equipo es {id}")
    print("\nS(si) y Enter(no)")
    audifonos = bool(input("Tiene audífonos? "))
    teclado = bool(input("Tiene teclado? "))
    mouse = bool(input("Tiene mouse? "))
    monitor = bool(input("Tiene monitor? "))
    if audifonos:
        audifonos = id
    else:
        audifonos = "No tiene"
    if teclado:
        teclado = id
    else:
        teclado = "No tiene"
    if mouse:
        mouse = id
    else:
        mouse = "No tiene"
    if monitor:
        monitor = id
    else:
        monitor = "No tiene"
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^15}{}{:^14}|".format(' ', 'SELECCION DE AREA DEL EQUIPO', ' '))
    print('+','-'*55,'+')
    print("1. Area de Training\n2. Area de Review")
    area = int(input("Selecciona una opción: "))
    if area == 1:
        os.system("clear")
        area = "Area Training"
        print('+','-'*55,'+')
        print("|{:^14}{}{:^14}|".format(' ', 'SELECCION DE LUGAR DEL EQUIPO', ' '))
        print('+','-'*55,'+') 
        print("1. Apolo\n2. Artemis\n3. Sputnik\n4. Skylab")
        lugar = int(input("Selecciona una opción: "))
        if lugar == 1:
            lugar = "Apolo"
        elif lugar == 2:
            lugar = "Artemis"
        elif lugar == 3:
            lugar = "Sputnik"
    elif area == 2:
        os.system("clear")
        area = "Area Review"
        print('+','-'*55,'+')
        print("|{:^14}{}{:^14}|".format(' ', 'SELECCION DE LUGAR DEL EQUIPO', ' '))
        print('+','-'*55,'+') 
        print("1. Corvus\n2. Endor")
        lugar = int(input("Selecciona una opción: "))
        if lugar == 1:
            lugar = "Corvus"
        elif lugar == 2:
            lugar = "Endor"
    data = {
        "area": {
            "area": area,
            "lugar": {
                "lugar": lugar,
                "idPc": id,
                "idAu": audifonos,
                "idT": teclado,
                "idM": mouse,
                "idMo": monitor,
            }
        }
    }

    diccEquipos["data"].append(data)
    core.crearInfo("equipos.json", data)

