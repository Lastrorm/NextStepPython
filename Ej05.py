#Crea un programa en Python que acepte una cadena de caracteres 
#y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh"). 
#El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.
def principal():
    cadena = input('Introduzca la cadena ')
    cadena = str(cadena)
    for i in range(len(cadena), 0, -1):
     inv  =  cadena[i]
     print(inv)
