import os
import pacientes
if __name__ == "__main__":
    isActivate = True
    opcion=0
    while isActivate:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^24}|".format(' ','Menu Pricipal',' '))
        print('+','-'*55,'+')
        print("1. Gestionar de pacientes")
        print("2. Gestionar de veterinarios")
        print("3. Gestion de citas medica")
        print("4. Salir")

        opcion = int(input(":)_"))
        if (opcion == 1):
            pacientes.LoadInfoPaciente()
            pacientes.Pacientes()
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            isActivate = False
        else:
            print("Opcion no valida....")
            input("Presione un tecla para continuar ....")