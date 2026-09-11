operacao = input("Digite a operação (+, -, *, /): ").strip()
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if operacao == "+":
    print("Resultado:", n1 + n2)
elif operacao == "-":
    print("Resultado:", n1 - n2)
elif operacao == "*":
    print("Resultado:", n1 * n2)
elif operacao == "/":
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Operação inválida.")
