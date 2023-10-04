import os
import trainer
import equipos
import incidencias

if __name__ == "__main__":
    isActivate = True
    opcion = 0
    while isActivate:
        os.system("clear")
        print('+','='*55,'+')
        print("|{:^24}{}{:^23}|".format(' ','CAMPUSLAND',' '))
        print('+','='*55,'+')
        print("|{:^22}{}{:^21}|".format(' ','Menu Principal',' '))
        print('+','='*55,'+')
        print("\n1. Registro De Trainer")
        print("2. Registro De Equipos")
        print("3. Registro De Incidencias")
        print("4. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                trainer.LoadInfoTrainer()
                trainer.RegisterTrainer()
            elif opcion == 2:
                equipos.LoadInfoEquipos()
                equipos.RegEquipos()
            elif opcion == 3:
                incidencias.LoadInfoIncidencias()
                incidencias.RegIncidencias()
            elif opcion == 4:
                isActivate = False
            else:
                print("Opción no válida....")
                input("Presione una tecla para continuar ....")
        except ValueError:
            print("¡Error! Por favor, ingresa un número válido.")
            input("Presione una tecla para continuar ....")