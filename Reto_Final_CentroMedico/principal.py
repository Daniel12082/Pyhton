import os 
import funciones
if __name__ == '__main__':
    isActive = True
    opcion = 0
    while isActive:
        os.system("clear")
        print("CAMPUSLAND MC")
        opcion=input("1. Agregar cita\n2. Buscar cita\n3. Modificar cita\n4. Cancelar cita\n5. Salir\nSeleccione una opcion: ")
        if opcion == "1":
            funciones.LoadInfoCitas()
            funciones.agregarCita()
        if opcion == "2":
            funciones.LoadInfoCitas()
            funciones.buscarCita()
        if opcion == "3":
            funciones.LoadInfoCitas()
            funciones.modificarCita()
        if opcion == "4":
            funciones.LoadInfoCitas()
            funciones.cancelarCita()
        if opcion == "5":
            isActive = False

        
