#   CLASES ABSTRACTAS:
#           -  NO LAS VAMOS A INSTANCIAR NUNCA DIRECTAMENTE.
#           - CONTIENEN POR LO MENOS UN METODO ABSTRACTO.
#           - LAS VAMOS A USAR DE BASE PARA SUBCLASES MAS ESPECIFICAS.
# 
#   METODOS ABSTRACTOS:
#           - DEBEMOS SOBREESCRIBIRLOS EN CADA UNA DE LAS SUBCLASES.
  
from abc import ABC, abstractclassmethod

class Personaje(ABC):
    @abstractclassmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.inventario = []
        self.nivel = 0

    @abstractclassmethod
    def atacar(self, objetivo):
        pass

    @abstractclassmethod
    def getStatus(self):
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")

    def subirNivel(self):
        self.nivel += 1

    def verInventario(self):
        print(f"inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)


class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.inventario = ["pocion de maná", "Grimorio"]
        self.inteligencia = 95

    def getStatus(self):
        print(f"Pertenece a la clase Mago")
        super().getStatus()

    def atacar(self,objetivo):
        objetivo.vida -= self.inteligencia*0.6
        print(f"la vida actual del objetivo es {objetivo.vida}")

    def saludar(self):
        print(f"hola soy un mago mi nombre es {self.nombre}")

    
class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.inventario = ["posicon de vida", "escudo", "espada"]
        self.fuerza = 100
    
    def getStatus(self):
        print("pertenesco a la clase guerrero")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza
        print(f"la vida acutual del objetivo es {objetivo.vida}")

    def saludar(self):
        print(f"hola soy un guerrero y mi nombre es {self.nombre}")
    
    



guerrero = Guerrero("thor")
mago = Mago("loki")
print("*****\n")
guerrero.saludar()
mago.saludar()
print("*****\n")
guerrero.getStatus()
mago.getStatus()
print("*****\n")
guerrero.verInventario()
print("*****\n")
mago.verInventario()
print("*****\n")
guerrero.atacar(mago)
mago.atacar(guerrero)






