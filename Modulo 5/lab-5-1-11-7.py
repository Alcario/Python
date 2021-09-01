def sacarEspacios(frase):
    frase2 = ""
    for letra in frase:
        if letra == " ":
            continue
        frase2 += letra
    return frase2

def palindromo(frase2):
    palindromo = ""
    for i in range(len(frase2)):
        palindromo += frase2[len(frase2) - 1 - i]
    return palindromo

def comparacion(frase1, fraseR):
    if frase1.upper() == fraseR.upper():
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

frase = input("Ingrese una frase: ")
if frase.isspace():
    print("No es un palíndromo.")
    frase = input("Ingrese una frase: ")

frase2 = sacarEspacios(frase)


palindromo = palindromo(frase2)

print(frase2)
print(palindromo)

comparacion(frase2, palindromo)