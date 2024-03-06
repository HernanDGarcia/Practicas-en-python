'''
    ARGUMENTOS

    *args  y **kwargs (key args) ----> pueden tener otros nombres *patitos

    *args
        Esto te devuelve un tupla que adentro tiene todos los argumentos

    **kwargs

    def function(*args)

    def function(**kwargs)

'''

def argumentos(*patitos):
    print(patitos)

argumentos(1, "hola", 3, [4,5])

def kwargumentos(**kwpatitos):
    print(kwpatitos)

kwargumentos(nombre = "diego", apellido= "garica", edad= 27 )


def suma(a,b):
    return a+b

def res(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

op = {
    1 : suma,
    2 : res ,
    3: mult,
    4: div,

}
#print(op["suma"](2,4))

print(''' eliga una opcion
    1)suma
    2)resta
    3)mult
    4)div
    
''')

eleccion = int(input("ingrese: "))
numa = int(input("dato a: "))
numb = int(input("dato b: "))
print(op[eleccion](numa, numb))
