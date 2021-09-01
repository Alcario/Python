miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
swapped = True
cantidad = []

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]
            
for i in range(len(miLista)-1):
    if miLista[i] == miLista[i + 1]:
        cantidad.append(i)
        
swapped = True

while swapped:
    swapped = False
    for i in range(len(cantidad) - 1):
        if cantidad[i] < cantidad[i + 1]:
            swapped = True
            cantidad[i], cantidad[i + 1] = cantidad[i + 1], cantidad[i]


for i in(cantidad):
    del miLista[i]
    
print("La lista solo con elementos únicos:")
print(miLista)
