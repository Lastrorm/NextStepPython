from datetime import datetime
def principal():
    while True:
        try:
            hora = datetime.strptime(input("Escribe una hora: "), '%H-%M')
        except ValueError:
            print("Formato de fecha incorrecto, debe ser dd/mm/yyyy")
        else:
            break

    if hora.hour <= 12:
        while True:
            try:
                ampm = input("Indica si la hora es AM o PM: ").upper
                if ampm != "AM" and ampm != "PM":
                    raise ValueError
            except ValueError:
                print("Debes escribir AM o PM")
            else:
                break


"""
#Algortimo hora24
from datetime import datetime
while True:
# Entrada
    try:
        hora,minus = input("Ingrese una hora en formato hh:mm ").split(":")
    except ValueError:
        print("Hora inválida. Por favor, ingrese una hora válida en formato hh:mm.")
        if int(hora) > 12:
            print(f"Su hora en formato 24H es las {hora}:{minus}")
            break
        if int(hora) <= 12:
            am_pm = input("¿Su hora es AM o PM? ").upper()
    # Proceso
            if am_pm == "AM":
                if int(hora) == 12:
                    hora = 00
                    horaconv = datetime(1,1,1, int(hora), int(minus))
                    hora12 = datetime.strftime(horaconv,"%H:%M")
                    # Salida
                    print(f"Su hora en formato 24H es las {hora12}")
                    break
                elif int(hora) < 12:
                    horaconv = datetime(1,1,1, int(hora), int(minus))
                    hora12 = datetime.strftime(horaconv,"%H:%M")
                    # Salida
                    print(f"Su hora en formato 24H es las {hora12}")
                    break
            elif am_pm == "PM":
                if int(hora) == 12:
                    horaconv = datetime(1,1,1, int(hora), int(minus))
                    hora12 = datetime.strftime(horaconv,"%H:%M")
                    # Salida
                    print(f"Su hora en formato 24H es las {hora12}")
                    break
                elif int(hora) < 12:
                    hora2 = int(hora)+12
                    horaconv = datetime(1,1,1,hora2,int(minus))
                    hora12 = datetime.strftime(horaconv,"%H:%M")
                    # Salida
                    print(f"Su hora en formato 24H es las {hora12}")
                    break
"""