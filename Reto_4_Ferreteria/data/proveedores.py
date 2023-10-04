import core
import os
diccProveedores = {"data":[]}
def LoadInfoProveedores():
    global diccProveedores
    if (core.checkFile("proveedores.json")):
        diccProveedores = core.LoadInfo("proveedores.json")
    else:
        core.crearInfo("proveedores.json",diccProveedores)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("pause")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE PROVEEDORES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar proveedores")
    print("3. Editar proveedores")
    print("4. Eliminar proveedores")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','REGISTRO DE PROVEEDORES',' '))
        print('+','-'*55,'+')
        data ={
            "id":input("Ingrese el Id del proveedores :"),
            "nombre":input("Ingrese el Nombre del proveedores :"),
            "email":input("Ingrese el Email del proveedores :"),
        }
        diccProveedores["data"].append(data)
        core.crearInfo("proveedores.json",data)

    elif (opcion == 2):
        LoadInfoProveedores()
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^19}{}{:^20}|".format(' ','BUSCAR DE PROVEEDORES',' '))
        print('+','-'*55,'+')
        codSerch = input("Ingrese el codigo del proveedor que desea buscar: ")
        for i,item in enumerate(diccProveedores["data"]):
            if codSerch in item["id"]:
                print(f'DATOS DEL PROVEEDOR CON EL ID {item["id"]}\n')
                print(f'NOMBRE DEL PROVEEDOR: {item["nombre"]}'.upper())
                print(f'EMAIL DEL PROVEEDOR: {item["email"]}')
        input("Presione una enter para continuar...")

    elif (opcion == 3):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^19}{}{:^19}|".format(' ','EDICION DE PROVEEDORES',' '))
        print('+','-'*55,'+')
        codSerch = input("Ingrese el codigo del proveedor que desea buscar: ")
        for i,item in enumerate(diccProveedores["data"]):
            if codSerch in item["id"]:
                print(f'EDICION DE DATOS DEL PROVEEDOR CON EL ID {item["id"]}\n')
                item["nombre"] = input("Ingrese el nuevo nombre del proveedor: ") or item["nombre"]
                item["email"] = input("Ingrese el nuevo email del proveedor: ") or item["email"]
                os.system("clear")
        data ={
            "id":input("Ingrese el Id del proveedor :"),
            "nombre":input("Ingrese el Nombre del proveedor :"),
            "email":input("Ingrese el Email del proveedor :"),
        }

        core.EditarData("proveedores.json",diccProveedores)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^19}{}{:^19}|".format(' ','ELIMINACION DE PROVEEDORES',' '))
        print('+','-'*55,'+')
        codSerch = input("Ingrese el codigo del proveedor que desea buscar: ")
        for i,item in enumerate(diccProveedores["data"]):
            if codSerch in item["id"]:
                itemdel = diccProveedores["data"].pop(i)
                diccProveedores["data"].pop(i)
        #SOBRE ESCRIBIR
                core.EditarData("proveedores.json",diccProveedores)
        #REGRESAR ELEMENTO BORRADO
                #core.crearInfo("proveedores.json",itemdel)
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()