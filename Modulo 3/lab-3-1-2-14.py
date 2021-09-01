bloques = int(input("Ingrese el número de bloques:"))
parar = bloques

for altura in range (1, parar):
    
    if altura<=bloques:
        if bloques-altura >= 0:
            bloques-=altura
        else:
            altura-=1
            break
    else:
        altura-=1
        print("Hola2")
        break
    
if altura<=0:
    altura=1
    
print("La altura de la pirámide:", altura)
