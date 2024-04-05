#Crea un diccionario vacío llamado perro
perro={
    #Añade nombre, color, raza, patas y edad al diccionario perro.
    'Nombre':'Firulais',
    'Color':'Canela Pasion',
    'Raza':'Pincher',
    'Patas':'4',
    'Edad':'4'
}
#Crea un diccionario de estudiante y añade nombre, apellido, sexo, edad, estado civil, habilidades, país, ciudad y dirección como claves del diccionario
estudiante={
    'Nombre':'Pepito',
    'Apellido':'Tamal',
    'Sexo':'Helicopteroapachedecombate',
    'edad':'20',
    'estadocivil':'soltero',
    'Habilidades':['Ingles', 'Aleman', 'Frances', 'Portugues', 'Eunuco'],
    'Pais':'Colombia',
    'Ciudad':'Bogota',
    'Direccion':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
#Obtén la longitud del diccionario del alumno
print(len(estudiante))
#Obtenga el valor de las habilidades y compruebe el tipo de datos, debe ser una lista
print(type(estudiante['Habilidades']))
#Modifique los valores de las habilidades añadiendo una o dos habilidades.
estudiante['Habilidades'].append('El anillo unico')
estudiante['Habilidades'].append('La Fuerza')
print(estudiante['Habilidades'])
#Comprobar si existen
print('Habilidades' in estudiante)
print('Auto' in estudiante)
#Obtener las claves del diccionario como una lista
keys=estudiante.keys()
print(keys)
#Obtener los valores del diccionario como una lista
valores=estudiante.values()
print(valores)
#Cambie el diccionario a una lista de tuplas utilizando el método items()
print(estudiante.items())
#Eliminar uno de los elementos del diccionario
estudiante.popitem()
print(estudiante)
#Borrar uno de los diccionarios
print(perro)
print(perro.clear())