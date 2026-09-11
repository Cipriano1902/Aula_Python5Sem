numero_secreto = 7

palpite = int(input("Adivinhe o número secreto entre 1 e 10: "))

while palpite != numero_secreto:
    print("Palpite incorreto.")
    palpite = int(input("Tente novamente: "))

print("Parabéns! Você acertou.")
