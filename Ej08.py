def leer():
    lista = []
    stop = False
    while stop == False:
        if len(lista) == 0:
            lista.append(input("Introduce el primer valor de la lista: "))
        else:
            print("¿Desea continuar? s/n: ", end="")
            decision = input().upper()
            if decision == "S":
                lista.append(input("Introduzca el siguiente valor de la lista: "))
            else:
                stop = True
    return lista

def principal():
    listaPalabras = leer()
    nuevalista = []


    for cadena in listaPalabras:
        if len(cadena.split()) > 5:
            nuevalista.append(cadena)

    print(f"La nueva lista con más de 5 palabras es: {nuevalista}")