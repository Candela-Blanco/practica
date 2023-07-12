try:
    resultado= 10/0
except ZeroDivisionError:
    print("No se puede dividir entre cero")


try: 
    resultado="2"+2
except TypeError:
    print("!error¡ No se pueden sumar caracteres con numeros")


lista=[1,2,3,4]

try:
    apuntar=lista[2]
except IndexError:
    print("Error el indice esta fuera del rango de la lista")