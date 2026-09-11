numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    print("Informe um número positivo.")
else:
    for i in range(numero, 0, -1):
        print(i)
