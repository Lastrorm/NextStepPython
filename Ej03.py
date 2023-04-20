# Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. 
# El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.
def principal():
     palabra = input('Introduzca la cadena de carateres ')
     try:
        palabra = str(palabra)
     except: 
        print('Introduce una cadena de texto valida') 
     else: #corregir
        salida = int(len(palabra.split(' ')))
     #salida
        print('El número de palabras es {s}'.format(s=salida))
    
        