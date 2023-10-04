import os
import campers
if __name__ == "__main__":
    isActivate = True
    opcion=0
    while isActivate:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^24}|".format(' ','Menu Pricipal',' '))
        print('+','-'*55,'+')
        print("1. Registro de campers")
        print("2. Lista campers")
        print("3. Buscar camper de campers")
        print("4. Edicion de campers")
        print("5. Eliminacion de camper")
        print("6. Salir")
        
        opcion = int(input(":)_"))
        if (opcion == 1):
            campers.LoadInfoCamper()
            campers.registro()
        elif (opcion == 2):
            campers.lista()
        elif (opcion == 3):
            campers.Buscar()
        elif (opcion == 4):
            pass
        elif (opcion == 5):
            pass
        elif (opcion == 6):
            isActivate = False
        else:
            print("Opcion no valida....")
            input("Presione un tecla para continuar ....")