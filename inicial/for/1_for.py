import random

numeros = [6, 5, 3, 2, 9, 10, 11]

#for num in numeros:
 #   print(num)

'''for i in range(10):
    print(i+1)
else:
    print("es el final") '''


# list comprehensions

'''[   expresion(i)   for i in list   if condición   ] '''

tabla2 = [(i+1)*2 for i in range(10) ]

#print(tabla2)

'''tab2 = []
for i in range(10):
    mul=(i+1)*2
    tab2.append(mul)

print(tab2)'''
    

alumnos = []

for i in range(30):
    notas = [random.randint(1, 10) for i in range(3)]
    alumnos.append(notas)

promedios = []

for i in range(30):
    notas = alumnos[i]
    suma = 0
    for nota in notas:
        suma += nota  

        promedio = round(suma /3)
    promedios.append(promedio)

print(promedios)
