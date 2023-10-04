import os
import funciones
if __name__ == "__main__":
    isActivate=True
    opcion=0
    while isActivate:
        os.system('clear')
        print('+','-'*56,'+')
        print(f'|{" ":^23} CAMPUS MD{" ":^25}|')
        print('+','-'*56,'+')
        print(f'|{" ":^22}MENU PRINCIPAL{" ":^22}|')
        print('+','-'*56,'+')
        print("1. Agregar cita")
        print("2. Buscar cita")
        print("3. Modificar cita")
        print("4. Cancelar cita")
        print("5. Salir")
        opcion = int(input("Seleccion una opcion: "))
        if opcion ==1:
            funciones.LoadInfoCitas()
            funciones.pedir_cita_medica()
        if opcion == 2:
            funciones.LoadInfoCitas()
            funciones.buscar_cita()
        if opcion == 3:
            funciones.LoadInfoCitas()
            funciones.modificar_cita()
        if opcion == 4:
            funciones.LoadInfoCitas()
            funciones.cancelar_cita()
        if opcion == 5:
            isActivate=False
        else:
            print("Opcion no valida")

