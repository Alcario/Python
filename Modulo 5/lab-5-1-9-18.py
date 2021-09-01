def misplit(cadena):
    if cadena.strip():
        return cadena.split(sep=" ")
    else:
        return "[]"

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))