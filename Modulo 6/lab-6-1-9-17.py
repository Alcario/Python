from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def init(self, message):
        StudentsDataException.init(self, message)

class FileEmpty(StudentsDataException):
    def init(self, message):
        StudentsDataException.init(self, message)

archivotxt = input("Nombre del archivo: ")

try:
    archivo = open(archivotxt, 'r')
except IOError as e:
    print("No se puede abrir el archivo", strerror(e.errno))
    exit()
try:
    biblioteca = {}

    read = archivo.readlines()
    archivo.close()
    for x in range(len(read)):
        temp = read[x].split()
        if len(temp) != 3:
            raise BadLine("Error: La siguiente línea no fué completada correctamente: " + str(x + 1))
        nombre = temp[0] + ' ' + temp[1]
        if nombre not in biblioteca:
            biblioteca[nombre] = float(temp[2])
        else:
            biblioteca[nombre] += float(temp[2])

except FileEmpty as fe:
    print(fe)
    exit(1)
except BadLine as bl:
    print(bl)
    exit(2)
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)

for nombre in sorted(biblioteca.keys()):
    print(nombre, biblioteca[nombre], "\n")
