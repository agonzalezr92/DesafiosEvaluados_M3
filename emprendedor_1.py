import math


"""# Actividad 2 - Rentabilidad

Un emprendedor quiere crear una app que provea un servicio de entrega de comida para
mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos
usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades
del proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

Donde:

P: Precio de Suscripción

U: Número de Usuarios

GT: Gastos Totales

Para ello, se te pide desarrollar este cálculo en tres versiones.

**Actividad 2 - Rentabilidad**
1. Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
(5 Puntos)

"""
print("Actividad 2 - Rentabilidad \n ")

p = float(input("Ingrese el precio de suscripción (en dólares): "))
u = int(input("Ingrese el número de usuarios: "))
gt = float(input("Ingrese los gastos totales (en dólares): "))


if (p < 0):
    print("El precio de suscripción no puede ser negativo")
    exit()

if (u < 0):
    print("El número de usuarios no puede ser negativo")
    exit()

if (gt < 0):
    print("Los gastos totales no pueden ser negativos")
    exit()

utilidades = p * u - gt

print(f"Las utilidades del proyecto son: {utilidades:.2f} dólares \n")