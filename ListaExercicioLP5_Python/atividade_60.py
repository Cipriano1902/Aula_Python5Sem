numero = int(input("Digite um número inteiro: "))

if numero == 0:
    print("O número 0 possui infinitos divisores inteiros não nulos.")
else:
    print(f"Divisores de {numero}:")
    for i in range(1, abs(numero) + 1):
        if numero % i == 0:
            print(i)
