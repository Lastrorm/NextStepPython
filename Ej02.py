 #Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. 
# El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.
import datetime
from distutils.config import PyPIRCCommand
import pytz
def principal():
    print (pytz.all_timezones)
    zona = input('Segun la lista. Introduzca su zona horaria para saber la hora exacta')
