def prueba(entrada, min, max):
    min = int(min)
    max = int(max)
    try:
        entrada = int(entrada)
        if entrada>min and entrada <max:
            return False
        else:
            return True

    except ValueError:
       return True

valor = input("Ingresa un número entre -10 a 10: ")
bandera = True
while bandera:
    bandera = prueba(valor, -10, 10)
    if bandera:
        print("entrada incorrecta")
        valor = input("Ingresa un número entre -10 a 10: ")

print("El número es: ", valor)


