numero = int(input("Digite um número de 0 a 20: "))

if not 0 <= numero <= 20:
    print("Número fora do intervalo de 0 a 20.")
elif 10 <= numero <= 15:
    print("O número está entre 10 e 15.")
else:
    print("O número não está entre 10 e 15.")
