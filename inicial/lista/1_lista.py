'''
listas 
'''

lista_1 = [2,4,8,5,3,99 ]

print(lista_1[0])
print(lista_1[-1])
print(lista_1[:1])
print(lista_1[1:])
print(lista_1[1:3])
print("ORDENANDO LISTA")
lista_1.sort()
print(lista_1)
print("ELIMINANDO ELEMENTOS DE LA LISTA")
del lista_1 [1:5]
print(lista_1)
print("SUMANDO ELEMENTOS DE LA LISTA")
res = sum(lista_1)
print(res)

'''
append() permite agregar UN elemento a la lista en el ultimo lugar

extend() permite agregar MAS DE UN elemento a la lista ejemplo: nums.extend([4,5,6])
nums = [1,2,3]  ----> nums = [1,2,3,4,5,6]

'''

lista_1.append(1)
print(lista_1)
lista_1.extend([3, 4, 5])
print(lista_1)

'''
las listas tambien se pueden multiplicar 
print(["hola"]*3)
Esto no altera nuestra lista inicial
'''
print(lista_1*3)

print(["hola"]*3)
print(lista_1)

'''
metodo insert(a, b)
nos permite agregar un elemento en la posicion deseada
donde 
- a es la posicion
- b es el elemento

'''

lista_1.insert(1, "hola")
print(lista_1)

'''
metodo del[a]
a es la posicion
este metodo elimina el dato de la posicion dada
del lista_1[1] -----> elimine el elemento 1 que es "hola"
tambien puedo eliminar varios elementos [1:4] 
quedando los elementos [2, ,4 ,5]
'''
print("METODO del")
del lista_1[1]
print(lista_1)
del lista_1[1:4]
print(lista_1)

'''
metodo remove()
el elemento remove  elimina el dato indicado en la lista
ej: remove(4)
'''

print("METODO remove")

lista_1.remove(4)
print(lista_1)

'''
metodo pop()
elimina el elemento segun su indice o si no se le indica elimina el ultimo elememto
'''

print("METODO pop")
lista_1.pop()
print(lista_1)

