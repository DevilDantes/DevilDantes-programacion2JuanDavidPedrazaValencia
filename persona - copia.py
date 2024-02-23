class persona:
    def __init__(self,nombre,apellido,cedulaint, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedulaint= cedulaint
        self.correo= correo
        self.telefono= telefono
    def obtenernombre(self):
        return f'mi nombre es {self.nombre} {self.apellido}'
    def obtenercedula(self):
        return f'mi cedula es {self.cedulaint}'
    def obtenercorreo(self):
        return f'mi correo es {self.correo}'
    def obtenertelefono(self):
        return f'mi correo es {self.telefono}'

p=persona("juan david","pedraza valencia", "1001974252", "juandavid.pedrazavalencia@unitecnar.edu.co" , "3207744389")
       
print("mi nombre es", p.obtenernombre(), "mi cedula es", p.obtenercedula(), "mi correo es" , p.obtenercorreo() , "y mi numero de telefono es", p.obtenertelefono())

