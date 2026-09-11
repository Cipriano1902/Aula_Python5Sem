nota = float(input("Digite uma nota de 0 a 10: "))

if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota < 5:
    print("Baixa")
elif nota < 8:
    print("Média")
else:
    print("Alta")
