''' 
EXCEPCIONES

    las excepciones son errores que ocurrern durante la ejecucion del programa
    Estos errores surgen a pesar de que la sintaxis sea correcta.
    Ejemplos:
        - Acceder a una posicicon de una lista superior a la logintud de este.
        - Intentar abrir un fichero que no existe.
        - Convertir "asdadfgfds" a int
        IMPORTANTE: Gestionar las excepciones nos permite que el código se siga
        ejecutando a pesar de los errores.

'''
import logging
#nos sirve para tener mas detalles del error

'''

def division(a, b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("no se puede dividir por cero")

division(5, 5)
division(5, 0)

print("hola")
'''

# gestion de distintos tipos de excepciones
'''
frutas = ["0- platano", "1- manzana", "2- naranja", "3- frutilla"]

def elegirFruta(listaFrutas):
    try:
        print(listaFrutas)
        index = int(input("Elige una fruta (pon el numero): "))
        print(f" tu fruta preferida es {listaFrutas[index]}")
    except IndexError:
        print(f"el indice es incorrecto eligue un numero del 0 al {len(listaFrutas)-1}")
    except ValueError:
        print("tiene que ser un numero entero")

elegirFruta(frutas)
elegirFruta(frutas)
elegirFruta(frutas)

'''




# Excepcion Exception
# Las excepciones son objetos que heredadn de la clase Exception.
'''

frutas = ["0- platano", "1- manzana", "2- naranja", "3- frutilla"]

def elegirFruta(listaFrutas):
    try:
        print(listaFrutas)
        index = int(input("Elige una fruta (pon el numero): "))
        print(f" tu fruta preferida es {listaFrutas[index]}")
    except Exception as error:
        logging.exception("el error es el siguiente")
        # print(error)

elegirFruta(frutas)
elegirFruta(frutas)
elegirFruta(frutas)
'''


# Else, finally, raise
# Vamos a sumar los números que nos pase el usuario separados por espacios:

while True:
    try:
        total = 0
        sumandos = input("Ponme números separados por espacios: ")
        sumandos = sumandos.split()
        for num in sumandos:
            if num.isnumeric():
                total += float(num)
            else:
                raise ValueError("El valor no es un número")

    except ValueError:
        print("los datos son incorrectos")
        print("vuelve a introducir los numeros")
    else:
        print(f"el resultado es {total}")
        break
    finally:
        print("ha terminado la iteracion")