def mostrar_tabuleiro(tabuleiro):
    print()
    for i, linha in enumerate(tabuleiro):
        print(" | ".join(linha))
        if i < 2:
            print("-" * 9)
    print()

def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for combinacao in combinacoes:
        if all(tabuleiro[l][c] == jogador for l, c in combinacao):
            return True
    return False

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador = "X"

print("JOGO DA VELHA")

while True:
    mostrar_tabuleiro(tabuleiro)

    try:
        linha = int(input(f"Jogador {jogador}, linha (1-3): ")) - 1
        coluna = int(input(f"Jogador {jogador}, coluna (1-3): ")) - 1
    except ValueError:
        print("Digite apenas números.")
        continue

    if not (0 <= linha <= 2 and 0 <= coluna <= 2):
        print("Posição inválida.")
        continue

    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada.")
        continue

    tabuleiro[linha][coluna] = jogador

    if verificar_vitoria(tabuleiro, jogador):
        mostrar_tabuleiro(tabuleiro)
        print(f"Jogador {jogador} venceu!")
        break

    if all(celula != " " for linha_tab in tabuleiro for celula in linha_tab):
        mostrar_tabuleiro(tabuleiro)
        print("Empate!")
        break

    jogador = "O" if jogador == "X" else "X"
