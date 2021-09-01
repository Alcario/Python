hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

print((hora+int((min+dura)/60))%24, (min+dura)%60)
