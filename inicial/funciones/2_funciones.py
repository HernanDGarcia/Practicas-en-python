''' 
VARIABLES LOCALES

    * variables inmutables {
        # int
        # string
        # float
        # tuppla
    }
        se crea una copia de esa variable

    * variable mutables {
        # listas
        # diccionarios
        # objetos
    }
        se crea una copia por referencia
            quiere decir que los cambios realizados en la funcion alteran
            a al variable pasada
'''

'''

def change_var(b):
    b = 5
    print(b)


a = [20]
print(a)
change_var1(a)
print(a)

'''
'''
def change_var1(b):
    b = [5]
    print(b)



a = [20]
print(a)
change_var1(a)
print(a)

resultado = [20] [5] [20]

'''
'''
def change_var1(b):
    b.append(5)
    print(b)

a = [20]
print(a)
change_var1(a)
print(a)

resultado = [20] [20, 5] [20, 5]
'''
'''
def change_var1(b=15):

    print(b)

a = [20]
print(a)
change_var1()
print(a)

resultado = [20], 15 [20]
'''
def change_var1(v, l=[]):
    l.append(v)
    return l



lrt1 = change_var1(2)
lrt2 = change_var1(4)
change_var1(5)
print(lrt1)


'''
VARIABLES LOCALES 

    son todas las que estan FUERA del entorno local
        ejemplo: CONSTANTES
'''