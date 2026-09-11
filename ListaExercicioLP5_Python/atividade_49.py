contador = 0

for i in range(1, 8):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > 10:
        contador += 1

print("Quantidade de números maiores que 10:", contador)
