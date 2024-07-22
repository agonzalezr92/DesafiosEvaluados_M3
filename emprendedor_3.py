import math

"""3. Considera ahora una tercera versión llamada emprendedor3.py. Necesitarás la
fórmula original de utilidades

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

Ahora, debes crear una nueva función en la que se pida (por medio de input()) los
siguientes datos:

● precio de suscripción P

● número de usuarios normales U

● gastos GT

● utilidades del año anterior Uanterior

El programa debe calcular las utilidades actuales Uactuales y mostrar la razón entre las
utilidades actuales y las del año anterior

𝑅𝑎𝑧ó𝑛 =
𝑈𝑎𝑐𝑡𝑢𝑎𝑙𝑒𝑠 /
𝑈𝑎𝑛𝑡𝑒𝑟𝑖𝑜𝑟

El resultado debe estar redondeado a dos decimales.(2 Puntos)
"""

p3 = float(input("Ingrese el precio de suscripción (en dólares): "))
u3 = int(input("Ingrese el número de usuarios normales: "))
gt3= float(input("Ingrese los gastos totales (en dólares): "))
uAnterior = float(input("Ingrese las utilidades del año anterior (en dólares): "))


if (p3 < 0):
    print("El precio de suscripción no puede ser negativo")
    exit()

if (u3 < 0):
    print("El número de usuarios no puede ser negativo")
    exit()

if (gt3 < 0):
    print("Los gastos totales no pueden ser negativos")
    exit()


uActuales = p3 * u3 - gt3

razon = (uActuales / uAnterior)

print(f"La utilidades actuales son: {uActuales:.2f}")
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.2f}")