import math


"""2. Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada precios
de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.
(3 Puntos)

"""

p2 = float(input("Ingrese el precio de suscripción para usuarios normales (en dólares): "))
u_normal = int(input("Ingrese el número de usuarios normales: "))
u_premium = int(input("Ingrese el número de usuarios premium: "))
gt2 = float(input("Ingrese los gastos totales (en dólares): "))


if (p2 < 0):
    print("El precio de suscripción no puede ser negativo")
    exit()

if (u_normal < 0):
    print("El número de usuarios normales no puede ser negativo")
    exit()

if (u_premium < 0):
    print("El número de usuarios premium no puede ser negativo")
    exit()

if (gt2 < 0):
    print("Los gastos totales no pueden ser negativos")
    exit()

utilidades2 = ((p2 * 1.5)* u_normal  + p2 * u_premium )- gt2

print(f"Las utilidades del proyecto son: {utilidades2:.2f} dólares \n")