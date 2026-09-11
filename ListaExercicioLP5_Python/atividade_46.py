soma = 0

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

media = soma / 10
print(f"Média: {media:.2f}")
