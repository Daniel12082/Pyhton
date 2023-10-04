import core
import os
diccCliente = {"data":[]}
def LoadInfoCliente():
    global diccCliente
    if (core.checkFile("clientes.json")):
        diccCliente = core.LoadInfo("clientes.json")
    else:
        core.crearInfo("clientes.json",diccCliente)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("pause")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CLIENTES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','REGISTRO DE CLIENTES',' '))
        print('+','-'*55,'+')
        data ={
            "id":input("Ingrese el Id del cliente :"),
            "nombre":input("Ingrese el Nombre del cliente :"),
            "email":input("Ingrese el Email del cliente :"),
        }
        diccCliente["data"].append(data)
        core.crearInfo("clientes.json",data)
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^19}{}{:^20}|".format(' ','BUSCAR DE CLIENTES',' '))
        print('+','-'*55,'+')
        codSerch = input("Ingrese el codigo del cliente que desea buscar: ")
        for i,item in enumerate(diccCliente["data"]):
            if codSerch in item["id"]:
                print(f'DATOS DEL CLIENTE CON EL ID {item["id"]}\n')
                print(f'NOMBRE DEL CLIENTE: {item["nombre"]}'.upper())
                print(f'EMAIL DEL CLIENTE: {item["email"]}')
        input("Presione una tecla para continuar...")

    elif (opcion == 3):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^19}{}{:^19}|".format(' ','EDICION DE CLIENTES',' '))
        print('+','-'*55,'+')
        codSerch = input("Ingrese el codigo del cliente que desea buscar: ")
        for i,item in enumerate(diccCliente["data"]):
            if codSerch in item["id"]:
                print(f'EDICION DE DATOS DEL CLIENTE CON EL ID {item["id"]}\n')
                item["nombre"] = input("Ingrese el nuevo nombre del cliente: ") or item["nombre"]
                item["email"] = input("Ingrese el nuevo email del cliente: ") or item["email"]
                os.system("clear")
        data ={
            "id":input("Ingrese el Id del cliente :"),
            "nombre":input("Ingrese el Nombre del cliente :"),
            "email":input("Ingrese el Email del cliente :"),
        }

        core.EditarData("clientes.json",diccCliente)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^19}{}{:^19}|".format(' ','ELIMINACION DE CLIENTES',' '))
        print('+','-'*55,'+')
        codSerch = input("Ingrese el codigo del cliente que desea buscar: ")
        for i,item in enumerate(diccCliente["data"]):
            if codSerch in item["id"]:
                itemdel = diccCliente["data"].pop(i)
                diccCliente["data"].pop(i)
        #SOBRE ESCRIBIR
                core.EditarData("clientes.json",diccCliente)
        #REGRESAR ELEMENTO BORRADO
                #core.crearInfo("clientes.json",itemdel)
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
hadsijhsajdh 

    
