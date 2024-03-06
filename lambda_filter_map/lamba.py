# estructura: lamba     arg1, arg2: expression

#FUNCIONES LAMBDA:
#   Son funciones anónimas (no tienen nombre):
#   - Permiten múltiples argumentos.
#   - Solo puede tener una exmpresión.
#   - Estructura: lambda arg1, arg2 : expression

suma = lambda a, b : a+b

print(suma(5,5))


maximo = lambda a, b, c: f"El maximo entre los numeros {a}, {b}, {c} es: {max(a, b, c)}"

print(maximo(1,2,3))

def Nombre(nombre):
    return lambda apellido: f"mi apellido es {apellido} y mi nombre es {nombre}"

nomApell = Nombre("Diego")

print(nomApell("garcia"))


def Dividir(divisor):
    return lambda dividendo: dividendo/divisor

numDiv = Dividir(5)
numDiv2 = Dividir(2)

print(numDiv(25))
print(numDiv2(8))