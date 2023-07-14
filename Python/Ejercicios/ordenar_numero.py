"""
Ordenamiento de números: 
Crea un programa que solicite al usuario tres números enteros y los muestre en orden ascendente.(no usar sort())
"""
número1= int(input("Ingrese el 1° número: "))
número2= int(input("Ingrese el 2° número: "))
número3= int(input("Ingrese el 3° número: "))

if número1 <= número2 and número1 <= número3:
    menor= número1
    if número2 <= número3:
        medio= número2
        mayor= número3
    else:
        medio= número3
        mayor= número2
elif número2 <= número1 and número2 <= número3:
    menor= número2
    if número1 <= número3:
        medio= número1
        mayor= número3
    else:
        medio= número3
        mayor= número1
elif número3 <= número2 and número3 <= número1:
    menor= número3
    if número2 <= número1:
        medio= número2
        mayor= número1
    else: 
        medio= número1
        mayor= número2
print (f"Los números en forma ascendente son: {menor, medio, mayor}")