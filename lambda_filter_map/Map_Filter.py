
# Funcion Filter.
# filter(function, iterable). Devuelve un iterador.
# con los valores del iterable que cumplan la función.


emails = [
    'javier@gmail.ar',
    'locura@hotmail.ar',
    'naranja',
    'escarabajo'
]

'''
emailValidos = []

for email in emails:
    if '@' in email:
        print(f'el {email} es valido')
        emailValidos.append(email)
    else:
        print(f'el {email} No es valido')


print(emailValidos)
'''

#def Filtro_email(email):
#   return '@' in email
   
'''if '@' in email:
        return True
    else:
        return False
'''


#emailValidos = list(filter(Filtro_email, emails))
#print(next(emailValidos))

emailValidos1 = list(filter(lambda email: '@' in email, emails))
print(emailValidos1)


# Función map
# map(function, iterable).
# Ejecuta la funcion usando como parametro cada elemento iterable.

palabras = ('hola', 'diego', 'buen')
longitudes = list(map(lambda palabra: len(palabra), palabras))

print(longitudes)