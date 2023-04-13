def principal():
    while True:
        try:
            num = input("Dame un número entero: ")
        except ValueError:
            print("El valor sólo puede ser un número entero")
        else:
            break

    sumatorio = 0

    if num > 0:
        for i in range(1, num):
            sumatorio += i
    elif num < 0:
        for i in range(num, 1):
            sumatorio += i
    else:
        sumatorio = 1

    print(f"La suma de todos los números desde el 1 hasta {num} es {sumatorio}")