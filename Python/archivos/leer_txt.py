# abrimos un archivo en modo lenctura y luego lo mostramos
# <utf-8> muestra todos los carácteres existentes, incluso 'ñ' 
archivo = open("Python\\archivos\\archivo.txt","r", encoding="utf-8")

contenido= archivo.read()

archivo.close()



archivo = open("Python\\archivos\\archivo.txt","r", encoding="utf-8")

for linea in archivo:
    print(linea)
    
archivo.close()

