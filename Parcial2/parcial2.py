class Personas:
    def __init__(self) :
        global user
        user=[]

    def menu(self):
        while True:
            print("\nMENU PERSONAS")
            print("1. Crear")
            print("2. Listar")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Personas.agregar())
            elif opcion == "2":
                print(Personas.listar())
            elif opcion == "3":
                print(Personas.refrescar())
            elif opcion == "4":
                print(Personas.eliminar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print ('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        nombre=input("ingrese su nombre: ")
        numerocc=input("ingrese el numero de cedula o tarjeta de identidad: ")
        genero=input("ingrese su genero: ")
        correo=input("ingrese su correo electronico: ")
        numerotel=input("ingrese su numero de telefono: ")
        user.append(nombre)
        user.append(numerocc)
        user.append(genero)
        user.append(correo)
        user.append(numerotel)
        return f'agreg1o el dato',nombre, numerocc, genero, correo, numerotel
    
    def listar():   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'los datos de la base de datos hasta ahora son',user
    
    def refrescar():
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        A=input("Ingrese la persona a actualizar ") 
        cambio=A in user   
        if(cambio==True):
            actualizar=input("ingrese el dato nuevo ")
            posicion=user.index(A)
            user[posicion]=actualizar
        

    def eliminar():
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        elim=input("ingrese el usuario a eliminar: ")
        user.remove(elim)
        return f'el usuario eliminado es',elim,'la lista actual es', user

class universidades:

    def __init__(self) :
        global user
        user=[]
    def menu2(self):
        while True:
            print("\nMENU Universidades")
            print("1. Crear")
            print("2. Listar")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(universidades.agregar())
            elif opcion == "2":
                print(universidades.listar())
            elif opcion == "3":
                print(universidades.refrescar())
            elif opcion == "4":
                print(universidades.eliminar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print ('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        Per=input("ingrese la universidad: ")
        user.append(Per)
        return f'agreg1o el dato',Per
    
    def listar():   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'los datos de la base de datos hasta ahora son',user
    
    def refrescar():
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        A=input("Ingrese la persona a actualizar ") 
        cambio=A in user   
        if(cambio==True):
            actualizar=input("ingrese el dato nuevo ")
            posicion=user.index(A)
            user[posicion]=actualizar
            
    def eliminar():
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        elim=input("ingrese el usuario a eliminar: ")
        user.remove(elim)
        return f'la universidad eliminado es',elim,'la lista actual es', user
    
class Notas:
    def __init__(self) :
        global user
        user=[]
    def menu3(self):
        while True:
            print("\nMENU Universidades")
            print("1. Crear")
            print("2. Listar")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Notas.agregar())
            elif opcion == "2":
                print(Notas.listar())
            elif opcion == "3":
                print(Notas.refrescar())
            elif opcion == "4":
                print(Notas.eliminar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print ('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        uni=input("ingrese las notas: ")
        user.append(uni)
        return f'agreg1o el dato',uni
    
    def listar():   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'los datos de la base de datos hasta ahora son',user
    
    def refrescar():
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        A=input("Ingrese la persona a actualizar ") 
        cambio=A in user   
        if(cambio==True):
            actualizar=input("ingrese el dato nuevo ")
            posicion=user.index(A)
            user[posicion]=actualizar
    
    def eliminar():
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        elim=input("ingrese la nota a eliminar: ")
        user.remove(elim)
        return f'la nota eliminado es',elim,'la lista actual es', user
class Asignatura:
    def __init__(self) :
        global user
        user=[]
    def menu4(self):
        while True:
            print("\nMENU Universidades")
            print("1. Crear")
            print("2. Listar")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Notas.agregar())
            elif opcion == "2":
                print(Notas.listar())
            elif opcion == "3":
                print(Notas.refrescar())
            elif opcion == "4":
                print(Notas.eliminar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print ('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        uni=input("ingrese las Asignaturas: ")
        user.append(uni)
        return f'agreg1o el dato',uni
    
    def listar():   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'los datos de la base de datos hasta ahora son',user
    
    def refrescar():
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        A=input("Ingrese la persona a actualizar ") 
        cambio=A in user   
        if(cambio==True):
            actualizar=input("ingrese el dato nuevo ")
            posicion=user.index(A)
            user[posicion]=actualizar
    
    def eliminar():
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        elim=input("ingrese la asignatura a quitar: ")
        user.remove(elim)
        return f'la asignatura eliminado es',elim,'la lista actual es', user              
            