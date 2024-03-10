class Vehiculo:
    def __init__(self, fecha_fabricacion, VIN_chasis, VIN_motor):
        self.fecha_fabricacion = fecha_fabricacion
        self.VIN_chasis = VIN_chasis
        self.VIN_motor = VIN_motor

    def obtener_fecha_fabricacion(self):
        return self.fecha_fabricacion

    def obtener_VIN_chasis(self):
        return self.VIN_chasis

    def obtener_VIN_motor(self):
        return self.VIN_motor

class Automovil(Vehiculo):
    def __init__(self, fecha_fabricacion, VIN_chasis, VIN_motor, marca, modelo, precio):
        super().__init__(fecha_fabricacion, VIN_chasis, VIN_motor)
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def obtener_marca(self):
        return self.marca

    def obtener_modelo(self):
        return self.modelo

    def obtener_precio(self):
        return self.precio

    def mostrar_datos(self):
        mensaje = f"Este automóvil es un {self.marca} {self.modelo}, fabricado en {self.fecha_fabricacion}."
        mensaje += f" Tiene un VIN de chasis {self.VIN_chasis} y un VIN de motor {self.VIN_motor}."
        mensaje += f" Su precio es {self.precio} dólares."
        print(mensaje)

auto1 = Automovil("2023", "ABC123", "XYZ789", "Toyota", "Corolla", 25000)

auto1.mostrar_datos()
