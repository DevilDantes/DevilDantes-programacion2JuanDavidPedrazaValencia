class lote:
    def __init__(self, largo, ancho, constructora,) :
        self.largo = largo
        self.ancho = ancho
        self.constructora = constructora
    def calculadorarea (self):
        print(self.ancho * self.largo)
        print(self.constructora)




class Casa(lote):
    def __init__(self, largo, ancho, constructora, propietario,telefono):
        super().__init__(largo, ancho, constructora)
        self.propietario = propietario
        self.telefono = telefono
    def printprpietario(self):
        print(self.propietario)
        print(self.telefono)
        
x = Casa(7,45, "Juan David Pedraza", "PepitoInc" , "3009934324")
x.calculadorarea()
x.printprpietario()
    