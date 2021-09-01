numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

n = int(input("ingrese un número entero: "))

while n != numeroSecreto:
    print("\"¡Ja, ja! ¡Estás atrapado en mi ciclo!\"")
    n = int(input("ingrese otro número entero: "))
print (n)
print("\"¡Bien hecho, muggle! Eres libre ahora\"")
