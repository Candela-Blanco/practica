Operación= str (input("Elija la operación: "))

Número_1= int (input("Ingrese un número: "))
Número_2= int (input("Ingrese el segundo número: "))

Suma= Número_1+Número_2
Resta= Número_1-Número_2
Multiplicación= Número_1*Número_2
División= Número_1/Número_2


if Operación == "Suma":
    print(f"La suma de los valores es igual a: {Suma}")
elif Operación == "Resta":
    print(f"La resta de los valores es igual a: {Resta}")
elif Operación == "Multiplicación":
    print(f"La multiplicación de los valores es igual a: {Multiplicación}")
elif Operación == "División":
    print(f"La división de los valores es igual a: {División}")
else:
    print(f"Elija una operación válida.")

        























