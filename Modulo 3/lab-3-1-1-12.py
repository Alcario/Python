ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso>=85528:
    impuesto=14839+(ingreso-85528)*0.32
else:
    impuesto=ingreso*0.18-556.02

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
