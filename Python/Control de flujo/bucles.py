edad = 22
#(3)cantidad de veces que se ejecuta el for
for i in range(3):
    edad=edad+edad
print (edad)


contador= 0

while True:
    edad = edad+edad
    contador += 1
    if contador == 3:
        break

print (edad)