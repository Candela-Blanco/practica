# declaramos una lista de diferentes tipos de datos
# las listas son modificables
# el argumento 1 es igual al indice 0, el argumento 2 es igual al indice 1, etc
# se puede apuntar a ningun indice
lista= ["Cande",22,True,1.57,]

lista[1]=35

print(lista)



# declaramos una tupĺa de diferentes tipos de datos
# las tuplas no son modificables pero si se pueden reconstruir
tupla= ("Cande",22,True,1.57,)

# tupla[1]=35 # esto no se puede hacer

tupla=("tupla reconstruida") #esto si, xq la estoy reconstruyendo


print(tupla)




# declaramos un conjunto de diferentes tipos de datos
# los conjuntos no se pueden modificar pero si reconstruir y tampoco se puede apuntar a ningun indice, y tamposo se pueden repetir valores
conjunto= {"Cande",22,True,1.57}

print(conjunto)





#declaramos un conjunto de diferentes tipos de datos
# los diccionarios se pueden modificar
# se puede apuntar a los índices
diccionario= {
    'Nombre': "cande",
    'edad': 22,
    'es_mayor':True,
    'Altura': 1.57,
}
diccionario['Nombre']="ezequiel"

print(diccionario)