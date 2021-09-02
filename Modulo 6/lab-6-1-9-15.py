from os import strerror

archivotxt = input("Nombre del archivo: ")

try:
    archivo = open(archivotxt, 'r')
except IOError as e:
    print("No se puede abrir el archivo", strerror(e.errno))
    exit()

biblioteca = {}

read = archivo.read().lower()

for letra in read:
    if letra.isalpha():
        if letra not in biblioteca.keys():
            biblioteca[letra] = 1
        else:
            biblioteca[letra] += 1

for letra, valor in sorted(biblioteca.items()):
    print(str(letra) + ' -> ' + str(valor))

archivo.close()
