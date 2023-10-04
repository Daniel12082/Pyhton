import core
import os
dicCompras={"data":[]}
def CreateData(*args):
    return core.LoadInfo("compras.json")

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^17}|".format(' ','ADMINISTRACION DE COMPRAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Devolucion")
    print("4. Anular compra")
    print("5. Regresar al menu principal")
    
    opcion =int(input(":)_"))
    
    if (opcion == 1):
        lista = []
        num=0
        dicProducto=core.LoadInfo("productos.json")
        for f,item in enumerate(dicProducto["data"]):
            print(item["id"],item["nombre"])
            
        for f,item in enumerate(dicProducto["data"]):    
            id=input("Ingrese el codigo del producto: ")
            if id in item["id"]:
                lista.append(item)
            else:
                input("")
        input("....")
    elif (opcion == 3):
        print(lista)
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
