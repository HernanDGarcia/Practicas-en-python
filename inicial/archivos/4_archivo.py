import json
diego = {
    'nombre': 'Diego',
    'edad': 27,
    'hobbies': [
        'dibujar'
        'leer'
        'programar'
        'entrenar'
        'musica'
    ],
    'hijos': None

}

with open("persona_diego.json", "w") as fo:
    json.dump(diego, fo)


# cargo el archivo json para poder cargarlo en la consola
with open("persona_diego.json", "r") as fi:
    persona = json.loads(fi.read())

print(persona)