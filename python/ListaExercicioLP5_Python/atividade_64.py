import random

numeros = [random.randint(1, 100) for _ in range(10)]
multiplos_de_3 = [numero for numero in numeros if numero % 3 == 0]

print("Lista aleatória:", numeros)
print("Múltiplos de 3:", multiplos_de_3)
