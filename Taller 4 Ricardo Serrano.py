import random

lista_ventas = []
for _ in range(30):
    valor = random.randint(1000000, 5000000)
    lista_ventas.append(valor)

total_ventas = 0
max_ventas = 0
dia_max_ventas = 0

for i in range(len(lista_ventas)):
    valor = lista_ventas[i]
    total_ventas += valor
    if valor > max_ventas:
        max_ventas = valor
        dia_max_ventas = i + 1

promedio_ventas = total_ventas / len(lista_ventas)

print(f"Las ventas del mes fueron: {lista_ventas}")
print(f"Total de ventas del mes: {total_ventas}")
print(f"Promedio de ventas diarias: {promedio_ventas}")
print(f"Día con las ventas más altas: Día {dia_max_ventas} con ventas de {max_ventas}")

