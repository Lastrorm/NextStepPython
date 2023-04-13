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
    for i in listaPalabras:
        if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i:
            nuevalista.append(i)

    print(f"La lista que contiene sólo palabras que tienen cadenas que poseen al menos una vocal es esta: {nuevalista}")