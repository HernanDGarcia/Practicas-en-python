class Circulo:
    def __init__(self, radio):
        self.__radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2*self.__pi*self.__radio

    def calcularArea(self):
        return self.__pi*self.__radio**2

# metodo publico para leer el valor de pi
    def getPi(self):
        return self.__pi

# metodo publico para cambiar el radio
    def setRadio(self, nuevoValor):
        if type(nuevoValor) == int or type(nuevoValor) == float():
            if nuevoValor > 0:
                self.radio = nuevoValor
                print(f"el radio se a modificado {self.__radio}")
            else:
                print("el radio no puede ser negativo")
        else:
            print("el radio tiene que ser un numero positivo")

c1 = Circulo(2.5)

print(c1.calcularArea())
print(c1.calcularPerimetro())
print(f"El valor de Pi: {c1.getPi()}")
c1.setRadio(34)
print(c1.calcularArea())
print(c1.calcularPerimetro())

#print(f"la constante Pi vale: {c1._Circulo__pi}")

# para encapsulacion privada
# atributo: __radio --> _Circulo__radio.    En general   _NombreDeLaClase__nombreDelAtributo
#lo que ocurre es que el inteprete de python automaticamente le cambia el nombre al nombre del atributo/metodo PRIVADO
# SIMPLEMENTE LE CAMBIA EL NOMBRE