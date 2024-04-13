from parcial2 import Personas
from parcial2 import universidades
from parcial2 import Notas
from parcial2 import Asignatura


def menu_principal():
    while True:
        print("MENU PRINCIPAL")
        print("1. Personas")
        print("2. Universidades")
        print("3. Notas")
        print("4. Asignatura")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            p = Personas()
            p.menu()
        elif opcion == "2":
            u = universidades()
            u.menu2()
        elif opcion == "3":
            n = Notas()
            n.menu3()
        elif opcion == "4":
            a = Asignatura()
            a.menu4()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")
menu_principal()
