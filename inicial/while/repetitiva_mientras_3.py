'''
script en Python que simule el sistema de validación de datos de una plataforma digital.
Se le solicitará al usuario su nombre y contraseña mientras la información proporcionada
no coincida con la informaciṕn previamente registrada.
'''

import os 
import time

USER = 'halub'
PASSWORD = 'puño'

user = ''
password = ''



while USER != user and PASSWORD != password:
    os.system('clear')

    user = input("usuario: ")
    password = input("password: ")

    if USER != user and PASSWORD != password:
        
        print(" el usuario y contraseña no coinciden")
        time.sleep(2)

    else:
        print("usuario y contraseña validos")