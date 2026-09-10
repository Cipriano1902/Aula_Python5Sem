n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Soma:", n1 + n2)
print("Subtração:", n1 - n2)
print("Multiplicação:", n1 * n2)

if n2 != 0:
    print("Divisão:", n1 / n2)
else:
    print("Divisão: não é possível dividir por zero.")
