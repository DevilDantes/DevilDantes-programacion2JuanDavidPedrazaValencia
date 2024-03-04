class factura:
    def __init__(self, id, vendedor, fechacompra):
        self.id=id
        self.vendedor=vendedor
        self.fechacompra=fechacompra
    def obtenerid(self):
        print(self.id)
    def obtenervendedor(self):
        print(self.vendedor)
    def obtenerfechadecompra(self):
        print(self.fechacompra)
        
class detallefactura(factura):
    def __init__(self, id, vendedor, fechacompra, producto, precio, cantidad):
        super().__init__(id, vendedor, fechacompra) #precio * cantidad
        self.producto=producto
        self.precio=precio
        self.cantidad=cantidad
    def productocomprado(self):
        print(self.producto)
    def cantidadcomprada(self):
        print(self.cantidad)
    def totaldecompra(self):
        print(self.precio*self.cantidad)
p=detallefactura("100045678", "Juan", "12/10/2024","Ryzen 5 5600g", 500000, 5)
p.obtenervendedor()
p.obtenerid()
p.obtenerfechadecompra()
p.productocomprado()
p.cantidadcomprada()
p.totaldecompra()

        