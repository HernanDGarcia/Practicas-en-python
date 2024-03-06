
import os
import random
import time
secreto = random.randint(1, 100)

inferior = 1
superior = 100
usuario = -1
maquina = -1

while usuario != secreto and maquina != secreto:
    os.system("clear")
    print('maquina eleccion')
    maquina = random.randint(inferior, superior)
    print(f'maquiena: {maquina}')
    if maquina > secreto:
        print("tu numero es mas grade")
        superior = maquina -1
        time.sleep(1)
    elif maquina < secreto:
        print("tu numero es mas chico")
        inferior = maquina +1
        time.sleep(1)
    else:
        print(f"adivinaste el numero es {secreto}")
        time.sleep(1)

    if maquina != secreto:
        usuario =int(input("seleccione un numero del 1 al 100:  "))
        if usuario > secreto:
            print("tu numero es mas grade")
            time.sleep(1)
            if usuario < superior:
                superior = usuario -1
        elif usuario < secreto:
            print("tu numero es mas chico")
            time.sleep(1)
            if usuario > inferior:
                inferior = 1 + usuario
        else:
            print(f"adivinaste el numero es {secreto}")
            time.sleep(1)
    input("Presione enter para continuar...")

input("adios")