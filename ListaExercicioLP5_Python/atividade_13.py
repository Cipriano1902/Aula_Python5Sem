mes = int(input("Digite um mês do ano (1 a 12): "))

# Estações aproximadas considerando o hemisfério sul.
if mes in (12, 1, 2):
    print("Verão")
elif mes in (3, 4, 5):
    print("Outono")
elif mes in (6, 7, 8):
    print("Inverno")
elif mes in (9, 10, 11):
    print("Primavera")
else:
    print("Mês inválido.")
