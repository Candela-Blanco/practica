"""
Cálculo de área y perímetro de un rectángulo:
Escribe un programa que solicite al usuario el ancho y el largo de un rectángulo, y luego calcule y 
muestre el área y el perímetro del rectángulo.
"""

ancho=float(input("Ingrese el ancho del rectángulo en metros: "))
largo=float(input("Ingrese el largo del rectángulo en metros: "))
área= ancho*largo
perímetro= (2*ancho) + (2*largo)
print(f"El área del rectángulo es: {área}")
print(f"El perímetro del rectángulo es: {perímetro}")