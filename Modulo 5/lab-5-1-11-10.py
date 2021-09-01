string1 = input("Ingrese una palabra: ").lower()
string2 = input("Ingrese una combinación de letras: ").lower()

cant=len(string1)
cont = 0
for letra in string1:
    if letra in string2:
        cont += 1
if cont != cant:
    print('No')
else:
    print('Si')