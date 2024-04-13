class Personas:
    def __init__(self):
        self.persona = []

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
                print(Personas.agregar(self))
            elif opcion == "2":
                print(Personas.listar(self))
            elif opcion == "3":
                print(Personas.refrescar(self))
            elif opcion == "4":
                print(Personas.eliminar(self))
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar(self):
        print ('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        nombre = input("Ingrese el nombre de la persona: ")
        edad = input("Ingrese la edad de la persona: ")
        sexo = input("Ingrese el sexo de la persona: ")
        cedula = input("Ingrese la cedula de la persona: ")
        direccion = input("Ingrese la direccion de la persona: ")
        self.persona.append({"nombre": nombre, "edad": edad, "sexo": sexo, "cedula":cedula, "direccion": direccion})
        print("el usuario ha sido creado con éxito.")

        return f'agreg1o el dato',nombre, edad, sexo, cedula, direccion
    
    def listar(self):   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'los datos de la base de datos hasta ahora son',self.persona
    
    def refrescar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        nombre = input("Ingrese el usuario a cambiar: ")
        for persona in self.persona:
            if persona['nombre'] == nombre:
                print("Ingrese los nuevos datos:")
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                sexo = input("Sexo: ")
                cedula = input("Cédula: ")
                direccion = input("Dirección: ")
                persona.update({"nombre": nombre, "edad": edad, "sexo": sexo, "cedula": cedula, "direccion": direccion})
                print("Datos de la persona actualizados con éxito.")
                return
        print("Usuario no encontrado.")

    def eliminar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        elim=input("ingrese el usuario a eliminar: ")
        self.persona.remove(elim)
        return f'el usuario eliminado es',elim,'la lista actual es', self.persona

class universidades:

    def __init__(self) :
        self.universidades = []

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
                print(universidades.agregar(self))
            elif opcion == "2":
                print(universidades.listar(self))
            elif opcion == "3":
                print(universidades.refrescar(self))
            elif opcion == "4":
                print(universidades.eliminar(self))
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar(self):
        print ('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        nombre = input("Ingrese el nombre de la universidad: ")
        direccion = input("Ingrese la direccion de la universidad: ")        
        self.universidades.append({"nombre": nombre, "direccion": direccion})
        return f'los datos ingresados',nombre, direccion
    
    def listar(self):   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'los datos de la base de datos hasta ahora son',self.universidades
    
    def refrescar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        nombre = input("Ingrese el nombre de la persona que desea actualizar: ")
        for universidad in self.universidades:
            if universidad['nombre'] == nombre:
                print("Ingrese los nuevos datos:")
                nombre = input("Nombre: ")
                direccion = input("Dirección: ")
                universidad.update({"nombre": nombre, "direccion": direccion})
                print("Datos de la Universidad actualizados con éxito.")
                return
        print("La Datos de la informacion no encotrados.")
            
    def eliminar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        elim=input("ingrese el usuario a eliminar: ")
        self.universidades.remove(elim)
        return f'la universidad eliminado es',elim,'la lista actual es', self.universidades
    
class Notas:
    def __init__(self) :
        self.notas = []

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
                print(Notas.agregar(self))
            elif opcion == "2":
                print(Notas.listar(self))
            elif opcion == "3":
                print(Notas.refrescar(self))
            elif opcion == "4":
                print(Notas.eliminar(self))
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar(self):
        print ('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        nota=input("ingrese las notas: ")
        self.notas.append(nota)
        return f'agreg1o el dato',nota
    
    def listar(self):   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'los datos de la base de datos hasta ahora son',self.notas
    
    def refrescar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        A=input("Ingrese la persona a actualizar ") 
        cambio=A in self.notas   
        if(cambio==True):
            actualizar=input("ingrese el dato nuevo ")
            posicion=self.notas.index(A)
            self.notas[posicion]=actualizar
      
    def eliminar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        elim=input("ingrese la nota a eliminar: ")
        self.notas.remove(elim)
        return f'la nota eliminado es',elim,'la lista actual es', self.notas
class Asignatura:
    def __init__(self) :
        self.Asignatura=[]

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
                print(Notas.agregar(self))
            elif opcion == "2":
                print(Notas.listar(self))
            elif opcion == "3":
                print(Notas.refrescar(self))
            elif opcion == "4":
                print(Notas.eliminar(self))
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar(self):
        nombre = input("Ingrese el nombre de la asignatura: ")
        profesor = input("Ingrese el nombre del profesor de la asignatura: ")
        self.Asignatura.append({"nombre": nombre, "profesor": profesor})
        print("Asignatura creada con éxito.")

    def listar_asignaturas(self):
        return f'agreg1o el dato',self.Asignatura
    
    def listar(self):   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        nombre = input("Ingrese el nombre de la asignatura que desea actualizar: ")
        for asignatura in self.Asignatura:
            if asignatura['nombre'] == nombre:
                print("Ingrese los nuevos datos:")
                n_nombre = input("Nuevo nombre de la asignatura: ")
                n_profesor = input("Nuevo nombre del profesor: ")
                asignatura['nombre'] = n_nombre
                asignatura['profesor'] = n_profesor
                print("Asignatura actualizada con éxito.")
                return
        print("La asignatura no se encontró.")     
        return f'los datos de la base de datos hasta ahora son',self.Asignatura
    
    def refrescar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
       
    
    def eliminar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        elim=input("ingrese la asignatura a quitar: ")
        self.Asignatura.remove(elim)
        return f'la asignatura eliminado es',elim,'la lista actual es', self.Asignatura              
        
