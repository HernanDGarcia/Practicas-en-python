'''
archivos delimitados
ejemplo: excel
'''
import random


with open("alumnos.csv") as fi:
    alumnos = []
    ln = fi.readline()
    while ln != "":
        alumnos.append(ln.replace("\n", "").split(","))#sacamos el espaciado \n y lo separamos 
        ln = fi.readline()
print(alumnos)


print("*****"*20+"\n")

'''
for alumno in alumnos:
    alumno.append(random.randint(1, 15))
    alumnos_nuevo.append(alumno)
'''

#alumnos_nuevo = [alumno.append(random.randint(1, 15)) for alumno in alumnos] NO FUNCIONA
# por que con esto estamos agregando un elemento a la lista original MODIFICANDOLA
#por eso llamamos a la lista alumnos

# agregamos las faltas al alumno
[alumno.append(str(random.randint(1, 15))) for alumno in alumnos] 

alumnos_nuevo = [",".join(alumno)for alumno in alumnos]
print(alumnos_nuevo)
print("*****"*20+"\n")
alumnos_nuevo = "\n".join(alumnos_nuevo)

print(alumnos_nuevo)

with open("alumnos_nuevo.csv","w") as out:
    out.write(alumnos_nuevo)