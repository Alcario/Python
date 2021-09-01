def mensaje():
    encript = 0
    while encript == 0:
        try:
            encript = int(input('Ingrese el valor de encriptación debe de estar entre 1-25: '))
            if encript not in range(1,26):
                raise ValueError
        except ValueError:
            print("El valor se encuentra fuera de rango")
            encript = 0
    return encript

def encriptador(text, encript):
    menEncript = ''
    for letra in text:
        if not letra.isalpha():
            menEncript += letra

        elif letra == " ":
            menEncript += letra

        elif letra.isupper() == True:
            code = ord(letra) + encript

            if code > ord('Z'):
                code = code + ord('A') - ord('Z') - 1

            menEncript += chr(code)

        elif letra.islower() == True:
            code = ord(letra) + encript

            if code > ord('z'):
                code = code + ord('a') - ord('z') - 1

            menEncript += chr(code)

        else:
            menEncript += letra
    return menEncript

print("El mensaje encriptado es: ", encriptador(input("Ingrese una mensaje: "), mensaje()))