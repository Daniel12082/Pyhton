import os
import core
diccTrainer={"data":[]}

def LoadInfoTrainer():
    global diccTrainer
    if (core.checkFile("trainer.json")):
        diccTrainer = core.LoadInfo("trainer.json")
    else:
        core.crearInfo("trainer.json",diccTrainer)

def RegisterTrainer():
    reg = True
    while reg:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^19}{}{:^19}|".format(' ', 'GESTION DE TRAINERS', ' '))
        print('+','-'*55,'+')
        print("1. Agregar trainer")
        print("2. Lista de trainers")
        print("3. Editar trainer")
        print("4. Eliminar trainer")
        print("5. Volver al menú principal\n")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            os.system("clear")
            print('+','~'*55,'+')
            print("|{:^20}{}{:^21}|".format(' ','REGISTRO TRAINER',' '))
            id = core.checkid("trainer.json")
            if id != False:
                data={
                    "id":id,
                    "nombre":input("Nombre: "),
                    "emailP":input("Email personal: "),
                    "email":input("Email Corporativo: "),
                    "telefono":int(input("Telefono: ")),
                    "telefonoR":int(input("Telefono Residencia: ")),
                    "telefonoE":int(input("Telefono Empresarial: ")),
                    "telefonoM":int(input("Telefono Movil Empresarial: "))
                }
                os.system("clear")
                print('+','-'*55,'+')
                print("|{:^19}{}{:^18}|".format(' ','ID DEL TRAINER',' '))
                print('+','-'*55,'+')
                print(f'EL ID DEL TRAINER ES EL {data["id"]}')
                input("Presione un enter para continuar ....")
                diccTrainer["data"].append(data)
                core.crearInfo("trainer.json",data)
            else:
                input("El usuario ya esta registrado\npresione enter para continuar ....")
        if opcion == 2:
            LoadInfoTrainer()
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^20}{}{:^20}|".format(' ','LISTA DE TRAINERS',' '))
            print('+','-'*55,'+')
            for i,item in enumerate(diccTrainer["data"]):
                print(f'|{" ":^13} DATOS DEL TRAINER CON EL ID {item["id"]}{" ":^12}|')
                print('+','-'*55,'+')
                print(f'{" ":^7}NOMBRE DEL TRAINER: {item["nombre"]}{" ":^16}'.upper())
                print(f'{" ":^7}EMAIL PERSONAL DEL TRAINER: {item["email"]}{" ":^11}')
                print(f'{" ":^7}TELEFONO PERSONAL DEL TRAINER: {item["telefono"]}{" ":^11}')
                print('+','-'*55,'+')

            input("Presione una enter para continuar...")
        if opcion == 3:
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^19}{}{:^19}|".format(' ','EDICION DEL TRAINER',' '))
            print('+','-'*55,'+')
            codSerch = input("Ingrese el codigo del trainer que desea buscar: ")
            for i,item in enumerate(diccTrainer["data"]):
                if codSerch in item["id"]:
                    print(f'EDICION DE DATOS DEL TRAINER CON EL ID {item["id"]}\n')
                    item["nombre"] = input("Ingrese el nuevo nombre del trainer: ") or item["nombre"]
                    item["emailP"] = input("Ingrese el nuevo emailP del trainer: ") or item["emailP"]
                    item["email"] = input("Ingrese el nuevo email del trainer: ") or item["email"]
                    item["telefono"] = input("Ingrese el nuevo telefono del trainer: ") or item["telefono"]
                    item["telefonoR"] = input("Ingrese el nuevo telefonoR del trainer: ") or item["telefonoR"]
                    item["telefonoE"] = input("Ingrese el nuevo telefonoE del trainer: ") or item["telefonoE"]
                    item["telefonoM"] = input("Ingrese el nuevo telefonoM del trainer: ") or item["telefonoM"]
                    os.system("clear")
            data={
                "nombre":item["nombre"],
                "emailP":item["emailP"],
                "email":item["email"],
                "telefono":item["telefono"],
                "telefonoR":item["telefonoR"],
                "telefonoE":item["telefonoE"],
                "telefonoM":item["telefonoM"]
            }
            
        if opcion == 4:
            os.system("clear")
            print('+',''*55,'+')
            print("|{:^19}{}{:^19}|".format(' ','ELIMINACION DE TRAINER',' '))
            print('+','-'*55,'+')
            codSerch = input("Ingrese el codigo del trainer que desea eliminar: ")
            for i,item in enumerate(diccTrainer["data"]):
                if codSerch in item["id"]:
                    diccTrainer["data"].pop(i)
                    core.EditarData("trainer.json",diccTrainer)
        if opcion == 5:
            reg = False
