fila1 = list(input("Ingresar 9 valores entre 0 y 9: "))
fila2 = list(input("Ingresar 9 valores entre 0 y 9: "))
fila3 = list(input("Ingresar 9 valores entre 0 y 9: "))
fila4 = list(input("Ingresar 9 valores entre 0 y 9: "))
fila5 = list(input("Ingresar 9 valores entre 0 y 9: "))
fila6 = list(input("Ingresar 9 valores entre 0 y 9: "))
fila7 = list(input("Ingresar 9 valores entre 0 y 9: "))
fila8 = list(input("Ingresar 9 valores entre 0 y 9: "))
fila9 = list(input("Ingresar 9 valores entre 0 y 9: "))



tablero = [[1 for i in range(9)] for j in range(9)]


tablero[0] = list(fila1)
tablero[1] = list(fila2)
tablero[2] = list(fila3)
tablero[3] = list(fila4)
tablero[4] = list(fila5)
tablero[5] = list(fila6)
tablero[6] = list(fila7)
tablero[7] = list(fila8)
tablero[8] = list(fila9)

subtab = tablero[:]

subtab[0] = [tablero[0][0:3], tablero[1][0:3], tablero[2][0:3]]
subtab[1] = [tablero[0][3:6], tablero[1][3:6], tablero[2][3:6]]
subtab[2] = [tablero[0][6:], tablero[1][6:], tablero[2][6:]]
subtab[3] = [tablero[3][0:3], tablero[4][0:3], tablero[5][0:3]]
subtab[4] = [tablero[3][3:6], tablero[4][3:6], tablero[5][3:6]]
subtab[5] = [tablero[3][6:], tablero[4][6:], tablero[5][6:]]
subtab[6] = [tablero[6][0:3], tablero[7][0:3], tablero[8][0:3]]
subtab[7] = [tablero[6][3:6], tablero[7][3:6], tablero[8][3:6]]
subtab[8] = [tablero[6][6:], tablero[7][6:], tablero[8][6:]]

colum = tablero[:]

colum[0] = [tablero[i][0] for i in range(9)]
colum[1] = [tablero[i][1] for i in range(9)]
colum[2] = [tablero[i][2] for i in range(9)]
colum[3] = [tablero[i][3] for i in range(9)]
colum[4] = [tablero[i][4] for i in range(9)]
colum[5] = [tablero[i][5] for i in range(9)]
colum[6] = [tablero[i][6] for i in range(9)]
colum[7] = [tablero[i][7] for i in range(9)]
colum[8] = [tablero[i][8] for i in range(9)]

check1 = []
check2 = []
check3 = []
finalcheck = []

for i in range(0,9):
    prueba = [1,2,3,4,5,6,7,8,9]
    for fila in subtab[i]:
        for caracter in fila:
            if int(caracter) in prueba:
                prueba.remove(int(caracter))
                check1.append(1)

if len(check1) == 81:
    finalcheck.append(1)

for filas in tablero:
    prueba = [1,2,3,4,5,6,7,8,9]
    for caracter in filas:
        if int(caracter) in prueba:
            prueba.remove(int(caracter))
            check2.append(1)


if len(check2) == 81:
    finalcheck.append(1)

for column in colum:
    prueba = [1,2,3,4,5,6,7,8,9]
    for caracter in column:
        if int(caracter) in prueba:
            check3.append(1)
            prueba.remove(int(caracter))

if len(check3) == 81:
    finalcheck.append(1)

if len(finalcheck) == 3:
    print("Si")

else:
    print("No")