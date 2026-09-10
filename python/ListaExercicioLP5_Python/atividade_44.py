pares = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    if numero % 2 == 0:
        pares.append(numero)

print("Números pares:", pares)
