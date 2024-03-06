class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def presentarce(self):
        print(f"hola mi nombre es {self.nombre}, tengo {self.edad} años")
"""
persona1 = Persona("Diego", 27, 546798)
persona1.presentarce()
print(persona1.DNI)"""


class Trabajador(Persona):
    def __init__(self, nombre, edad, DNI, sueldo, cargo, empresa):
        super().__init__(nombre, edad, DNI)
        self.sueldo = sueldo
        self.cargo = cargo
        self.empresa = empresa

    def calcularSuedoAnual(self):
        return 12*self.sueldo

"""
trabajador1 = Trabajador("juan", 33, 27984, 1500, "programador", "google")
trabajador1.presentarce()
sueldo1 = trabajador1.calcularSuedoAnual()
print(sueldo1)
"""

class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI, universidad, curso, asignaturas):
        super().__init__(nombre, edad, DNI)
        self.universidad = universidad
        self.curso = curso
        self.asignaturas = asignaturas

    def describirse(self):
        print(f"""hola soy {self.nombre}, tengo {self.edad} años. 
        Estudio en la universidad de {self.universidad}, estoy en la carrera de {self.curso},
        estoy en las asignaturas de {self.asignaturas}""")


estudiante1 = Estudiante("Sofia", 23, 465469, "universidad de lanus", "liceciatura en nutricion", ["curso de ingreso", "la universidad en arg " ,"tecnicas universitarias"])

estudiante1.describirse()