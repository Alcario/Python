palabra = input("Ingresa una frase: ")
palabra2 = input("Ingresa otra frase: ")

palabra = palabra.replace(" ", "")
palabra2 = palabra2.replace(" ", "")

frase = []

for caracter in palabra.lower():
    if caracter in palabra2.lower():
        frase.append(1)
    else:
        frase.append(0)

if 0 not in frase:
    print("Anagramas")

else:
    print("No son anagramas")