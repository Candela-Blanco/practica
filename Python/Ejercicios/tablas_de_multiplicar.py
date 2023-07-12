"""
Generador de tablas de multiplicar:
Escribe un programa que solicite al usuario un número entero y muestre por pantalla la
tabla de multiplicar de ese número, desde 1 hasta 10.

"""
"""
número1= int(input("Ingrese número de tabla"))
números= [1,2,3,4,5,6,7,8,9,10]
for valores in números:
    print ()
"""
"""
número1= int(input("Ingrese número de tabla: "))

valor_de_tabla= 0

while True:
    resultado= número1*valor_de_tabla
    print (f"{número1} x {valor_de_tabla} = {resultado}")
    if valor_de_tabla == 10:
        break 
    valor_de_tabla += 1
"""

numero=int(input("Ingresa el numero del cual quieres la tabla: "))
for i in range(11):
    print(f"{numero}*{i}= {numero*i}")