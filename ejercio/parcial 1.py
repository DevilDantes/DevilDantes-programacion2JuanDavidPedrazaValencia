class animales:
    def __init__(self,nombre,numerodepatas,fechadevacuna,propietario):
        self.nombre=nombre
        self.numerodepatas = numerodepatas
        self.fechadevacuna = fechadevacuna
        self.propietario = propietario
    def obtenernombre(self):
        return f'{self.nombre}'
    def obternernumerodepatas(self):
        return f'{self.numerodepatas}'
    def obternerfechadevacuna(self):
        return f'{self.fechadevacuna}'
    def obternerpropietario(self):
        return f'{self.propietario}'
a=animales("Bob marly","4","04/03/2024","Juan David")
print("el nombre del animal es:",a.obtenernombre(),"el numero de patas del animal:",a.obternernumerodepatas(),"el fecha de vacuna es:",a.obternerfechadevacuna(),"el nombre del propietario es:",a.obternerpropietario())
        
        