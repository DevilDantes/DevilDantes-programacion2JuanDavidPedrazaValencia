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
                print("Datos del usuario actualizados con éxito.")
                return
        print("Usuario no encontrado.")

    def eliminar(self):
        nombre = input("Ingrese el nombre de usuario que desea eliminar: ")
        for persona in self.persona:
            if persona['nombre'] == nombre:
                self.persona.remove(persona)
                print("El usuario ha sido eliminado con éxito.")
                return
        return f'el usuario eliminado es',persona,'la lista actual es', self.persona

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
        nombre = input("Ingrese los datos de la universidad que desea actualizar: ")
        for universidad in self.universidades:
            if universidad['nombre'] == nombre:
                print("Ingrese los nuevos datos:")
                nombre = input("Nombre: ")
                direccion = input("Dirección: ")
                universidad.update({"nombre": nombre, "direccion": direccion})
                print("Datos de la Universidad actualizados con éxito.")
                return
        print("La Datos de la universidad no encotrados.")
            
    def eliminar(self):
        nombre = input("Ingrese el nombre de la universidad que desea eliminar: ")
        for universidad in self.universidades:
            if universidad['nombre'] == nombre:
                self.universidades.remove(universidad)
                print("Universidad a sido eliminada éxitosamente    .")
                return
        print("La universidad no encontrada.")
    
class Notas:
    def __init__(self) :
        self.notas = []

    def menu3(self):
        while True:
            print("\nMENU Notas")
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
        return f'el dato de la nota',nota
    
    def listar(self):   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'las nota hasta ahora son',self.notas
    
    def refrescar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        A=input("Ingrese la nota a actualizar ") 
        cambio=A in self.notas   
        if(cambio==True):
            actualizar=input("ingrese la nueva nota a actualizar ")
            posicion=self.notas.index(A)
            self.notas[posicion]=actualizar
      
    def eliminar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        Notas = int(input("Ingrese la nota que desea eliminar: "))
        for nota in self.notas:  
            if nota == str(Notas):  
                self.notas.remove(nota)
            print("La nota fue eliminada con éxito.")
            return
        print("La nota no se encontró.")

class Asignatura:
    def __init__(self) :
        self.Asignatura=[]

    def menu4(self):
        while True:
            print("\nMENU Asignatura")
            print("1. Crear")
            print("2. Listar")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Asignatura.agregar(self))
            elif opcion == "2":
                print(Asignatura.listar(self))
            elif opcion == "3":
                print(Asignatura.refrescar(self))
            elif opcion == "4":
                print(Asignatura.eliminar(self))
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar(self):
        nombre = input("Ingrese el nombre de la asignatura: ")
        profesor = input("Ingrese el nombre del profesor de la asignatura: ")
        self.Asignatura.append({"nombre": nombre, "profesor": profesor})
        print("Asignatura creada con éxito.")

    def listar(self):   
        print("HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR")
        return f'las asignatura hasta ahora son',self.Asignatura
    
    def refrescar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR")
        nombre = input("Ingrese el nombre de la asignatura que desea actualizar: ")
        for asignatura in self.Asignatura:
            if asignatura['nombre'] == nombre:
                print("Ingrese los nuevos datos:")
                nuevo_nombre = input("Nuevo nombre de la asignatura: ")
                nuevo_profesor = input("Nuevo nombre del profesor: ")
                asignatura['nombre'] = nuevo_nombre
                asignatura['profesor'] = nuevo_profesor
                print("Asignatura ha sido actualizada con éxito.")
                return
        print("La asignatura no se fue encontrada.") 
    
    def eliminar(self):
        print("HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR")
        nombre = input("Ingrese el nombre de la asignatura que desea eliminar: ")
        for asignatura in self.Asignatura:
            if asignatura['nombre'] == nombre:
                self.Asignatura.remove(asignatura)
                print("Asignatura eliminada con éxito.")
                return
        print("La asignatura no se encontró.")         
        

