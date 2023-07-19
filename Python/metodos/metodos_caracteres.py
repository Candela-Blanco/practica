text= "hola me llamo cande tengo 22 años y mido 1.57 metros"

# devuelve una copia de la cadena con el primer caracter en mayusculas y el resto en minusculas
primera_mayus = text.capitalize()

# devuelve una copia de la cadena en minusculas
minusculas= text.lower()

# devuelve una copia de la cadena en mayusculas
mayus= text.upper()

# devuelve una copia de la cadena con cada palabra en mayusculas
titulo= text.title()


# devuelve True si el comienzo de la cadena original empieza con la cadena dada
prefix= text.startswith("h")

# devuelve True si el final de la cadena original empieza con la cadena dada
suffix= text.endswith("metros")

# devuelve una lista de la cadena original

cortar= text.split(" ")


# remplza algo de la cadena original por la nueva cadena dada
remplazo= text.replace("22","35")


# devuelve la cantidad de veces que esta la cadena dada en la cadena original
contar= text.count("a")

# devuelve la posicion de la primera aparicon de la cadena dada o -1 sin no encuentra nada
encontrar= text.find("3")

# devuelve la posicion de la primera aparicon de la cadena dada o una exepcion sin no encuentra nada
encontrar2= text.index("a")

# devuelve True si la cadena contiene solo letras
solo_letras= text.isalpha()

# devuelve True si la cadena contiene solo digitos
solo_digitos= text.isdigit()

# devuelve True si la cadena contiene solo minusculas
solo_minusculas= text.islower()

#devuelve True si la cadena contiene solo mayusculas
solo_mayusculas= text.isupper()

#devuel la cantidad de caracteres de la cadena
#función
contar_todo= len(text)

#concatenando texto
text= "hola "
nombre="cande"

new= text + nombre

print("hola me llamo cande \n y estoy aprendiendo python")