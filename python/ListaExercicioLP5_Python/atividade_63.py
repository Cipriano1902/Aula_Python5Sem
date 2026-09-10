numeros = []

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)

print("Soma:", sum(numeros))
