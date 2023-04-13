def principal():
    cadena = input("Dame una cadena de caracteres: ")
    obsoleta = input("Dame aquella parte de la cadena que quieras reemplazar: ")
    reemplazo = input("Dame aquello con lo que vamos a reemplazar la palabra anterior: ")
    cambioistrue = False

    while cambioistrue != True:
        nuevacadena = cadena.replace(obsoleta, reemplazo)
        cambioistrue = True

    print(f"La nueva cadena ha quedado así: {nuevacadena}")