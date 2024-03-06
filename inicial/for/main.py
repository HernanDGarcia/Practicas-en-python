import nombres
import random

noms = nombres.get_nombres()
alumnos = {}

for nombre in noms:
    notas = [random.randint(1, 10) for i in range(3)]
    alumnos[nombre] = notas

promedios = {}

for nom in alumnos:
    nota = alumnos[nom] #estoy llamando a la lista del alumno diego:[7, 8, 9]
    suma = 0
    for n in nota:
        suma += n
    promedio = round(suma/3)
    promedios[nom]= promedio

print(promedios)
'''
valores_ordenados = sorted(promedios.values())
dict_ordenado= {}

for nota_ord in valores_ordenados:
    for nom_ord in promedios.keys():
        if promedios[nom_ord] == nota_ord:
            valores_ordenados[nom_ord] = promedios[nom_ord]
            break

print(dict_ordenado)'''