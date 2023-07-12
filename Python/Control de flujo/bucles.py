
# recorer una lista con un for in
lista= ["cande",22,True,1.57]

for valores in lista:
    print(valores)



# contar con un for
for num in range(1, 6):
    print(num)

# recoremos una cadena de caracteres con un for in
mensaje = "hola cande"
for carater in mensaje:
    print(carater)


#correr por un diccionario con un for in
estudiante={
    'nombre': "cande",
    'edad': 22,
    'curso':"python"
}
for clave, valor in estudiante.items():
    print(f"{clave} : {valor}")



contador= 0

while True:
    edad = edad+edad
    contador += 1
    if contador == 3:
        break

print (edad)

