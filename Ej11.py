def leer():
    lista = []
    stop = False
    while stop == False:
        if len(lista) == 0:
            while True:
                try:
                    lista.append(int(input("Introduce el primer valor de la lista: ")))
                except ValueError:
                    print("El valor debe ser un número entero")
                else:
                    break
        else:
            print("¿Desea continuar? s/n: ", end="")
            decision = input().upper()
            if decision == "S":
                while True:
                    try:
                        lista.append(int(input("Introduce el siguiente valor de la lista: ")))
                    except ValueError:
                        print("El valor debe ser un número entero")
                    else:
                        break
            elif decision == "N":
                stop = True
    return lista

def principal():
    listaNum = leer()
    suma = 0

    for num in listaNum:
        if num % 3 == 0:
            suma += num

    print(f"El valor total de la suma de todos los números pares es: {suma}")