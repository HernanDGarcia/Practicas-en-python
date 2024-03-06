class Camiseta:
    def __init__(self, marca, precio, talla, color):
        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color
        self.rebaja = False


    def Descuento(self, procentaje):
        self.precio = self.precio - self.precio*procentaje/100
        if procentaje < 100:
            self.rebaja = True
    
    def Info_producto(self):
        info = f"informacion del producto:\nMarca: {self.marca}\nPrecio: {self.precio:.2f}$\nTalla: {self.talla}\nColor: {self.color}"
        if self.rebaja:
            info += "\nEsta en REBAJA."
        return info

camiseta = Camiseta("gaucho", 50, "XL", "marron")
camiseta.Descuento(50)

Nikecamiseta = Camiseta("Nike", 100, "M", "blanco")


print(camiseta.Info_producto())
print("#######\n")
print(Nikecamiseta.Info_producto())