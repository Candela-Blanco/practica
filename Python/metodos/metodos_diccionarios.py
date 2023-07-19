diccionario={
    'nombre': "Cande",
    'edad': 22,
    'curso':"python",
    'es_mayor': True
}

diccionario2={
    'nombre': "ezequiel",
    'edad': 22,
    'curso':"python"
}

# devuelve todas las keys que contiene el diccionario
keys=diccionario.keys()

# devuelve todas llos values que contiene el diccionario
valores=diccionario.values()

# devielve una tupla por cada conjunto de key y value
items=diccionario.items()

# devuelve el value de de la key dada
obtener=diccionario.get("edad")

# elimna la clave y su valor de la key dada
elimina=diccionario.pop("edad")

# cambia los valores del <diccionario2> para hacerlos coinsider con el diccionario
diccionario2.update(diccionario)
print(diccionario2)
