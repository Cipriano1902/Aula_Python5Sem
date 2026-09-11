valor = float(input("Digite o valor do produto: R$ "))
desconto = valor * 0.10
valor_final = valor - desconto

print(f"Desconto de 10%: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
