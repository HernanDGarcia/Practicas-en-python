class Perro:
    #atributos
    '''
    nombre = "Pichu"
    color = "blanco"
    tamaño = "chico"
    '''
    def __init__(self, nombre, color, tamaño):
        self.nombre = nombre
        self.color = color
        self.tamaño = tamaño

    #Metodos
    def dormir(self):
        print(f"{self.nombre} esta durmiendo")
    def ladrar(self):
        print(f"{self.nombre} GUA, GUA")
    def correr(self):
        print("Corro")
    def dar_pata(self):
        print("toma la pata")

p1 = Perro("pichu", "blanco", "chico")
p2 = Perro("bulon", "negro", "grande")
p2.dormir()
p1.ladrar()
p1.dar_pata()
