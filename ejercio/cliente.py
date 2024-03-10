from datetime import datetime
class Clientes:
    def __init__(self, cedula, nombre, apellido, telefono, correo, direccion, fecha_nacimiento):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_valores(self):
        return self.cedula, self.nombre, self.apellido, self.telefono, self.correo, self.direccion, self.fecha_nacimiento
    def calcular_edad(self):
        fecha_nacimiento = datetime.strptime(self.fecha_nacimiento, "%Y/%m/%d")
        hoy = datetime.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad


cliente1 = Clientes("1001974252", "Juan David", "Pedraza Valencia", "3207744389", "juandavid.pedrazavalencia@unitecnar.edu.co", "Avenida Principal Carrera 30", "2001/10/12")

cedula, nombre, apellido, telefono, correo, direccion, fecha_nacimiento = cliente1.obtener_valores()
edad = cliente1.calcular_edad()

print(f"Mi nombre es {nombre} {apellido} y vivo en {direccion} y tengo {edad}.")
