#1. Crea un programa en Python que acepte una fecha como cadena de caracteres 
#en formato `"dd/mm/aaaa"` y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero. 

from datetime import datetime
def principal():
    n= input('Introduce una fecha en formato dd/mm/aaaa')
    try:
     fecha= datetime.strptime(n,'%d/%m/%Y')
    except ValueError:
     print('El formato introducido no es correcto')
    else:
     print(f"{fecha.year}-{fecha.month}-{fecha.day}")
