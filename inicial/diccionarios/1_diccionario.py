mi_dic ={"nombre": "Diego",
        "edad": 3, 
        "verdad" :True}

print(mi_dic)
print("***"*4)
# AGREGAR UNA KEY Y su Elemento
mi_dic["apellido"]= "Garcia"
print(mi_dic)
print("***"*4)

# Imprimir las llaves y los valores
for key, value in mi_dic.items():
    print(key)
    print(value)

# saber si existe cierto valor
if "apellido" in mi_dic:
    print("esta la llave apellido")
else:
    print("no existe la key apellido")