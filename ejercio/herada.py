class Person:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def printname(self):
        print(self.nombre, self.apellido)

class estudiante(Person):
    def __init__(self.nombre, apellido, edad):
        self.edad = edad
        Person.__init__(self, nombre, apellido, asignatura)
    