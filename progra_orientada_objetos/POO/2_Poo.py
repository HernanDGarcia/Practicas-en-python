import random

class Personaje:
    #funcion para obtener stats al azar
    # una sola bara _new_stat significa que este metodo solo debe ser usado por este objeto
        def _new_stat(self):
            dados = [random.randint(1, 6) for i in range(4)]
            dados.sort()
            max_dados = dados[1:]
            return sum(max_dados)

# le damos el nombre al personaje y sus diferentes atributos
        def __init__(self, nombre):
            self.nombre = nombre

            self.fuerza = self._new_stat()
            self.agilidad = self._new_stat()
            self.inteligencia = self._new_stat()
            self.energia = self._new_stat()

        def show(self):
            return f'''{self.nombre}
            fuerza: {self.fuerza}
            agilidad: {self.agilidad}
            inteligencia: {self.inteligencia}
            energia: {self.energia}
            '''

P1 = Personaje("LYNK")

print(P1.show())