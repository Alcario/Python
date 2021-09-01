cumple = input("¿Cuándo es tu cumpleaños? (formatos AAAAMMDD - AAAADMM - MMDDAAAA): ")

while len(cumple) != 8:
    cumple = input('Intente de nuevo: ')

sumacumple = 0

for number in cumple:
    sumacumple += int(number)

string = str(sumacumple)

sumacadena = 0
for val in string:
    sumacadena += int(val)
if sumacadena > 9:
    string = str(sumacadena)
    sumacadena2 = 0
    for val in string:
        sumacadena2 += int(val)
    print("Tú Dígito de la Vida es: ", sumacadena2)
else:
    print("Tú Dígito de la Vida es: ", sumacadena)
