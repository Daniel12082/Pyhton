import os
import core
diccPacientes={"datos":[]}

def LoadInfoPaciente():
    global diccPacientes
    if (core.checkFile("pacientes.json")):
        diccPacientes = core.LoadInfo("pacientes.json")
    else:
        core.crearInfo("pacientes.json",diccPacientes)
def Pacientes():
    os.system("clear")
    reg = True
    while reg == True:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','GESTION DE PACIENTES',' '))
        print('+','-'*55,'+')
        print("1. Agregar paciente")
        print("2. Buscar paciente")
        print("3. Mostrar informacion de un paciente")
        print("4. Volver al menu principal\n")
        opcion = int(input("Seleccion una opcion: "))
        if opcion == 1:
            os.system("clear")
            id = str(len(diccPacientes["datos"]) + 1).zfill(3)
            print('+','-'*55,'+')
            print("|{:^18}{}{:^1}|".format(' ','DATOS DEL PACIENTE',' '))
            print('+','-'*55,'+')
            bandera_Nom=True
            while bandera_Nom:
                Nombre_p=input("\nIngrese nombre del paciente: ").upper()
                nombres_registrados = [item["NombreP"] for item in diccPacientes["datos"]]
                if Nombre_p in nombres_registrados:
                    print("El NOMBRE YA ESTA REGISTRADO")
                else:
                    Nombre_paciente=Nombre_p
                    bandera_Nom=False
            Edad=int(input("Ingrese sus edad: "))
            Nombre_dueño=input("Ingrese nombre del dueño: ").upper()
            T = int(input("TIPO DE ANIMARL\nn1. Perro\n2. Gato\n3. Reptil\n4. Ave\nSeleccione una opcion: "))
            print("\nRazas")
            if T == 1:
                Tipo = "Perro"
                R = int(input("Tipo de animal\n1. Labrador Retriever\n2. Golden Retriever\n3. Bulldog\n4. Chihuahua\n5. Otro\nSeleccione una opcion: "))
                if R == 1:
                    Raza = "Labrador Retriever"
                if R == 2:
                    Raza = "Golden Retriever"
                if R == 3:
                    Raza = "Bulldog"
                if R == 4:
                    Raza = "Chihuahua"
                if R == 5:
                    Raza = input("Ingrese la raza: ")
            elif T == 2:
                Tipo = "Gato"
                R = int(input("Tipo de animal\n1. Siameses\n2. Persas\n3. Bengala\n4. Maine Coon\n5. Otro\nSeleccione una opcion: "))
                if R == 1:
                    Raza = "Siameses"
                if R == 2:
                    Raza = "Persas"
                if R == 3:
                    Raza = "Bengala"
                if R == 4:
                    Raza = "Maine Coon"
                if R == 5:
                    Raza = input("Ingrese la raza: ")
            elif T == 3:
                Tipo = "Reptil"
                R = int(input("Tipo de animal\n1. Boa constrictor\n2. Cocodrilo del Nilo\n3. Gecko leopardo\n4. Iguana verde\n5. Otro\nSeleccione una opcion: "))
                if R == 1:
                    Raza = "Boa constrictor"
                if R == 2:
                    Raza = "Cocodrilo del Nilo"
                if R == 3:
                    Raza = "Gecko leopardo"
                if R == 4:
                    Raza = "Iguana verde"
                if R == 5:
                    Raza = input("Ingrese la raza: ")
            elif T == 4:
                Tipo = "Ave"
                R = int(input("Tipo de animal\n1. Águila\n2. Búho\n3. Colibrí\n4. Flamenco\n5. Otro\nSeleccione una opcion: "))
                if R == 1:
                    Raza = "Águila"
                if R == 2:
                    Raza = "Búho"
                if R == 3:
                    Raza = "Colibrí"
                if R == 4:
                    Raza = "Flamenco"
                if R == 5:
                    Raza = input("Ingrese la raza: ")
            else:
                print("Opcio erronea")

            datos ={"NombreP":Nombre_paciente,
                    "Edad":Edad,
                    "NombreD":Nombre_dueño,
                    "Tipo":Tipo,
                    "Raza":Raza,
                    "id":id,
                    "citas":0
                    }
            os.system("Clear")
            print('+','-'*55,'+')
            print("|{:^16}{}{:^15}|".format(' ','ID DEL PACIENTE',' '))
            print('+','-'*55,'+')
            print(f'EL ID DE SU MASCOTA ES EL {datos["id"]}')
            input("Presione un enter para continuar ....")
            diccPacientes["datos"].append(datos)
            core.crearInfo("pacientes.json",datos)

        elif opcion == 2:
            dicc=core.LoadInfo("pacientes.json")
            search=True
            while search:
                os.system("clear")
                idSearch = (input("Ingrese el numero de id de su mascota: "))
                for i,item in enumerate(dicc["datos"]):
                    if idSearch == item["id"]:
                        os.system("clear")
                        print('+','-'*55,'+')
                        print(f'|{" ":^7} {i+1}. informacion del la macosta con el id {item["id"]} {" ":^7}|'.title())
                        print('+','-'*55,'+')
                        print(f'Nommbre: {item["NombreP"]}'.title())
                        print(f'Edad: {item["Edad"]}')
                        print(f'Nombre del dueño: {item["NombreD"]}'.title())
                        print(f'Tipo: {item["Tipo"]}'.title())
                        print(f'Raza: {item["Raza"]}'.title())
                    else:
                        print("MASCOTA NO REGISTRADA")
                    search = bool(input(("Desea buscar otra Mascota S(si) Enter(No)")))
        elif opcion == 3:
            dicc=core.LoadInfo("pacientes.json")
            search=True
            while search:
                os.system("clear")
                idSearch = (input("Ingrese el numero de id de su mascota: "))
                for i,item in enumerate(dicc["datos"]):
                    if idSearch == item["id"]:
                        os.system("clear")
                        print('+','-'*55,'+')
                        print(f'|{" ":^7} {i+1}. informacion del la macosta con el id {item["id"]} {" ":^7}|'.title())
                        print('+','-'*55,'+')
                        print(f'Nommbre: {item["NombreP"]}'.title())
                        print(f'Edad: {item["Edad"]}')
                        print(f'Nombre del dueño: {item["NombreD"]}'.title())
                        print(f'Tipo: {item["Tipo"]}'.title())
                        print(f'Raza: {item["Raza"]}'.title())
                        print(f'Citas {item["Historial".title()]}')
                    else:
                        print("MASCOTA NO REGISTRADA")
                    search = bool(input(("Desea buscar otra Mascota S(si) Enter(No)")))
        elif opcion == 4:
            reg = False
            