class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola mi nombre es {self.nombre}")

class Perro(Mascota):
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y soy un perro")

class Gato(Mascota):
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y soy un gato")

class Pajaro(Mascota):
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y soy un pajaro")

if __name__ == '__main__': 

    '''todo lo que esta dentro de  if __name__ == '__main__': 
    se ejecutara solo cuando se llame al archivo ejemplo: animales.py
    si este modulo es llamado a otro archivo esta porcion de codigo no se ejecutara
    '''
    p1 = Perro("pichu")
    g1 = Gato("miya")
    b1 = Pajaro("Pepe")

    p1.saludar()
    g1.saludar()
    b1.saludar()

''' esta porcion del codigo que no esta dentro del if __name__ == '__main__': 
se podra ejecutar si el modulo es llamado la otra parte no 
pero el print("hola") si se ejecutara
ejemplo en el archivo main.py llamamos al modulo animales y se imprime el
print("hola")'''
print("hola NO estoy identado en el if __name__ == '__main__': ")
print(__name__)