#Calculadora de Índice de Masa Corporal
"""Escribe un programa que solicite al usuario su peso en kilogramos y su altura en metros, y calcule el IMC
utilizando la fórmula: IMC = peso / (altura^2). Luego, muestra el resultado y clasifica el IMC en una de las
siguientes categorías:
Peso inferior al normal (Menos de 18.5)
Peso Normal (18.6 - 24.9)
Peso superior al normal (25.0 - 29.9)
Obesidad (más de 30.0)
"""
peso= int(input("Ingrese su peso en kg: "))
altura= float(input("Ingrese su altura en metros: "))
IMC= peso/(altura**2)
print(f"Su IMC es de: {IMC}")
if IMC <= 18.5:
    print("Por lo tanto su peso es inferior al peso normal.")
elif IMC >= 18.6 and IMC <= 24.9:
    print("Por lo tanto su peso es normal.")
elif IMC >= 25.0 and IMC <= 29.9:
    print ("Por lo tanto su peso es superior al peso normal.")
elif IMC >= 30.0:
    print("Por lo tanto su peso es calificado como obesidad.")
    