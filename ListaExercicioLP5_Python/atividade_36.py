numero = int(input("Digite um número de 1 a 12: "))

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

if 1 <= numero <= 12:
    print(meses[numero - 1])
else:
    print("Número inválido.")
