import os
import Ej01
import Ej02
import Ej03
import Ej04
import Ej05
import Ej06
import Ej07
import Ej08
import Ej09
import Ej10
import Ej11

while True:
    os.system('cls') #limpia pantalla
    print('Bienvenidos')
    print('1- Cambio formato fecha de "dd/mm/aaaa" a "aaaa-mm-dd"')
    print('2- Mostrar hora exacta según zona horaria')
    print('3-Saber número de palabras según zona horaria')
    print('4-Pasar de formato de hora de 12H a 24H')
    print('5-Invertir cadena de texto')
    print('6- Sumar todos los numeros del 1 al numero dado')
    print('7-Imprimir las letras de una cadena en lineas separadas')
    print('8- Devolver las cadenas de una lista con más de 5 caracteres')
    print('9-reemplazar una palabra en una cadena de texto')
    print('10-Devuelve a partir de una lista de caracteres otra lista con las cadenas que tienen al menos una vocal ')
    print('11-devolver números multiplos de 3')
    opcion = input('seleccione programa a ejecutar')

    if opcion == '1':
        Ej01.principal()
    elif opcion == '2':
        Ej02.principal()
    elif opcion =='3':
        Ej03.principal()
    elif opcion == '4':
        Ej04.principal()
    elif opcion == '5':
        Ej05.principal()
    elif opcion == '6':
        Ej06.principal()
    elif opcion == '7':
        Ej07.principal()
    elif opcion == '8':
        Ej08.principal()
    elif opcion == '9':
        Ej09.principal()
    elif opcion == '10':
        Ej10.principal()
    elif opcion == '11':
        Ej11.principal()
    elif opcion == '0' :
      print('Un placer, hasta la proxima')
    break  
      
