''' 
script en python que muestre un menú con distintos personajes de un videojuego.
Si el usuario selecciona alguno de los personajes, se le mostrarán sus caracteristicas
El menú será el cíclico y se mostrará mientras el usuario no indique que desea salir.
'''
import os

MAGO = 1
GUERRERO = 2
SACERDOTISA = 3
SALIR = 4

#bandera para salir
continuar = True

while continuar:
    print("Elige tu campion")
    print(f'''
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir
    ''')

    eleccion = int(input("seleccione un personaje: "))

    if eleccion == MAGO:
        print("tu campion es un MAGO")
    elif eleccion == GUERRERO:
        print("tu campion es un GUERRERO")
    elif eleccion == SACERDOTISA:
        print("tu campion es una SACERDOTISA")
    elif eleccion == SALIR:
        print("adios")
        continuar = False
    else:
        print("opcion no valida")
    input("presiona enter para continuar")

input("nos vemos")

    
    


