def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    print()
    print("    1   2   3")
    for i, linha in enumerate(tabuleiro, start=1):
        print(f"{i}   " + " | ".join(linha))
        if i < 3:
            print("   ---+---+---")
    print()

def verificar_vitoria(tabuleiro, jogador):
    linhas = tabuleiro
    colunas = [[tabuleiro[l][c] for l in range(3)] for c in range(3)]
    diagonais = [
        [tabuleiro[i][i] for i in range(3)],
        [tabuleiro[i][2 - i] for i in range(3)],
    ]

    combinacoes = linhas + colunas + diagonais
    return any(all(celula == jogador for celula in combinacao)
               for combinacao in combinacoes)

def tabuleiro_cheio(tabuleiro):
    return all(celula != " " for linha in tabuleiro for celula in linha)

def ler_jogada(tabuleiro, jogador):
    while True:
        try:
            linha = int(input(f"Jogador {jogador}, escolha a linha (1-3): ")) - 1
            coluna = int(input(f"Jogador {jogador}, escolha a coluna (1-3): ")) - 1
        except ValueError:
            print("Entrada inválida. Digite números de 1 a 3.")
            continue

        if not (0 <= linha < 3 and 0 <= coluna < 3):
            print("Posição fora do tabuleiro.")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já possui uma jogada. Escolha outra.")
            continue

        return linha, coluna

def jogar_partida():
    tabuleiro = criar_tabuleiro()
    jogador = "X"

    while True:
        mostrar_tabuleiro(tabuleiro)
        linha, coluna = ler_jogada(tabuleiro, jogador)
        tabuleiro[linha][coluna] = jogador

        if verificar_vitoria(tabuleiro, jogador):
            mostrar_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            return

        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("Empate! Não há mais jogadas possíveis.")
            return

        jogador = "O" if jogador == "X" else "X"

def main():
    print("JOGO DA VELHA")

    while True:
        jogar_partida()
        resposta = input("Deseja iniciar uma nova partida? (s/n): ").strip().lower()

        if resposta not in ("s", "sim"):
            print("Jogo encerrado.")
            break

if __name__ == "__main__":
    main()
