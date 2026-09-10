combustivel = input("Digite o combustível (gasolina, etanol, diesel): ").strip().lower()

# Valores apenas ilustrativos para o exercício.
if combustivel == "gasolina":
    print("Preço ilustrativo: R$ 6,00 por litro.")
elif combustivel == "etanol":
    print("Preço ilustrativo: R$ 4,00 por litro.")
elif combustivel == "diesel":
    print("Preço ilustrativo: R$ 6,20 por litro.")
else:
    print("Combustível inválido.")
