# Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. 
# El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.
def principal():
    palabra = input('Introduzca la cadena de carateres ')
    palabra = str(palabra)
    i=0
    while i<len(palabra):
     i=i+1
     print(f'La cadena tiene {i} letras')