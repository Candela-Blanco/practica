"""
Suma de elementos de una lista: 
Escribe un programa que sume todos los elementos de una lista de números enteros y muestre el resultado 
por pantalla. no usar (sum())
lista=[22,23,24,25,2,8,7]
"""
lista=[22,23,24,25,2,8,7]
suma= 0
for número in lista:
    suma += número
print(f"La suma total de los números es: {suma}")