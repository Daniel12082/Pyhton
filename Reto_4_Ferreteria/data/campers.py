import os
import core
diccCampers = {"datos":[]}
def LoadInfoCamper():
    global diccCampers
    if (core.checkFile("campers.json")):
        diccCampers = core.LoadInfo("campers.json")
    else:
        core.crearInfo("campers.json",diccCampers)

def registro():
    os.system("clear")
    reg = True
    while reg:
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','REGISTRO DE CAMPER',' '))
        print('+','-'*55,'+')
        datos = {
                "Nombre":input("Ingrese sus nombres: ").upper(),
                "Apellidos":input("Ingrese sus apellidos: ").upper(),
                "Edad":int(input("Ingrese sus edad: ")),
                "Id":int(input("Ingrese sus numero de identificacion: ")),
                "Email":input("Ingrese su correo electronico: ").upper(),
                "Ciudad de origen":input("Ingrese su ciudad de origen:").upper(),
                "Estado civil":input("Ingrese su estado civil: ").upper(),
                "Genero":input("Ingrese su genero(M o F): ").upper(),
                "Nro Telefonico":int(input("Ingrese su numero de telefono: ")),
            }
        if (datos["Edad"]<18):
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^20}{}{:^24}|".format(' ','DATOS DE ACUDIENTE',' '))
            print('+','-'*55,'+')
            acudiente = {
                "Nombre:":input("Ingrese nombre completo de su acudiente: ").upper(),
                "Parentesco: ":input("Ingrese el parentesco de su acudiente: ").upper(),
            }
            datos["acudiente"]=acudiente
            diccCampers["datos"].append(datos)
            core.crearInfo("campers.json",datos)
        else:
            diccCampers["datos"].append(datos)
            core.crearInfo("campers.json",datos)
    reg =bool(input(("Desea registrar otro camper S(si) Enter(No)")))
def lista():
    os.system("clear")
    dicc=core.LoadInfo("campers.json")
    for i,item in enumerate(dicc["datos"]):
        print(f'{i+1}. informacion del camper {item["Nombre"]} {item["Apellidos"]}'.title())
        print(f'Edad: {item["Edad"]}'.title())
        print(f'Id: {item["Id"]}'.title())
        print(f'Email: {item["Email"]}'.title())
        print(f'Ciudad de origen: {item["Ciudad de origen"]}'.title())
        print(f'Estado civil: {item["Estado civil"]}'.title())
        print(f'Genero: {item["Genero"]}'.title())
        print(f'Nro Telefonico: {item["Nro Telefonico"]}'.title())
        input("Presione una tecla para continuar . . . . ")

def Buscar():
    os.system("clear")
    dicc=core.LoadInfo("campers.json")
    search=True
    while search:
        os.system("clear")
        idSearch = int(input("Ingrese el numero de identificacion del estudiante: "))
        for i,item in enumerate(dicc["datos"]):
            if idSearch == item["Id"]:
                os.system("clear")
                print('+','-'*55,'+')
                print(f'|{" ":^9} {i+1}. informacion del camper {item["Nombre"]} {item["Apellidos"]} {" ":^9}|'.title())
                print('+','-'*55,'+')
                print(f'Edad: {item["Edad"]}'.title())
                print(f'Email: {item["Email"]}'.title())
                print(f'Ciudad de origen: {item["Ciudad de origen"]}'.title())
                print(f'Estado civil: {item["Estado civil"]}'.title())
                print(f'Genero: {item["Genero"]}'.title())
                print(f'Nro Telefonico: {item["Nro Telefonico"]}'.title())
                search = bool(input(("Desea buscar otro camper S(si) Enter(No)")))
                