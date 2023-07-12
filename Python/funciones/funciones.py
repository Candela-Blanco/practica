
# creamos una funcion que saluda
def saludarr():
    print ("hola!!")


# LLamamos a la funcion creada
#saludar()

def saludar(nombre):
    print(f"hola {nombre} como estas?")


#saludar("eze")


def saludar_amigo(nombre="amigo"):
    print(f"hola {nombre} como estas?")

#saludar_amigo()
#saludar_amigo("cande")



def sumar(a,b):
    return a+b


resultado=sumar(4,5)
print (resultado)