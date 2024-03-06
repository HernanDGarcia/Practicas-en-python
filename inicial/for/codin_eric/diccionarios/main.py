'''
Coding-eric video 11
diccionarios
'''

mi_dic = {"nombre": "Eric", "edad": 3, "verdad": True}

# for key, value in mi_dic.items():
# 	print(key)
# 	print(value)

# if "apellido" in mi_dic:
# 	print("hay edad")

# mi_dic["apellido"] = "codin"

import random
import nombres

# print(nombres.get_nombres())

noms= nombres.get_nombres()
alumnos = {}

for nombre in noms:
	notas = [random.randint(1, 10) for i in range(3)]
	alumnos[nombre] = notas


promedios = {}
for nom in alumnos:
	notas = alumnos[nom]
	suma = 0
	for nota in notas:
		suma = nota + suma
	promedios[nom] = suma / 3

print(promedios)



