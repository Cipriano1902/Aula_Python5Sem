cidade = input("Digite o nome de uma cidade: ").strip().lower()

if cidade in ("brasília", "brasilia"):
    print("É a capital do Brasil.")
else:
    print("Não é a capital do Brasil.")
