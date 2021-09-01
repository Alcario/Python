listaSombrero = [1, 2, 3, 4, 5]

listaSombrero[int(len(listaSombrero)/2)]=int(input("ingrese un valor: "))

del listaSombrero[-1]

print(len(listaSombrero))

listaSombrero.append(22)

print(listaSombrero)
