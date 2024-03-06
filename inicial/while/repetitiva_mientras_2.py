'''
script en python que sume valores pares y multiplique valores impares mientras el
usuario no ingrese un 0. Se deberá utilizar la estructura repetitiva "mientras" para 
solicitar al usuario un número y dependiendo del número lo suma o lo multiplica.
'''

print("Programa que suma los números pares y multiplica los impares")

SUMA = 0
MULTIPLICA = 1

numero = -1

while numero != 0:
    numero = int(input("ingrese un numero (0 para salir):  "))
    if numero % 2 == 0 :
        SUMA += numero
    else:
        MULTIPLICA *= numero

    print(f'suma : {SUMA}')
    print(f'multiplizacion: {MULTIPLICA}')
