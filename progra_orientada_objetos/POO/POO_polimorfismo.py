class Empleado:
    def __init__(self, nombre, sueldoMensual):
        self.nombre = nombre
        self.sueldoMensual = sueldoMensual

    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1+1/100)
        print(f"El sueldo anual de {self.nombre}, empleado normal, es de {sueldo}")

class Contable(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1+4/100)
        print(f"El sueldo anual de {self.nombre}, de un Contable, es de {sueldo}")

class Publicista(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1+5/100)
        print(f"El sueldo anual de {self.nombre}, de un publisista, es de {sueldo}")



empleados = [
    Empleado("juan", 1000),
    Contable("melani", 1200),
    Publicista("albert", 1500)
]

for empleado in empleados:
    empleado.calcularSueldoAnual()