'''
archivos binarios y de texto

 "w" write
 "r" read

'''

datos = "hola mundo 2222"

file = open("datos.txt", "w")
file.write(datos)
file.close()

with open("data.txt", "w") as archivos:
    archivos.write(datos)

with open("datos.txt", "r") as archivos:
    texto = archivos.read()

print(texto)