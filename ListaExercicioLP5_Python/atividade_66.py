nomes = []

def listar():
    if not nomes:
        print("Nenhum nome cadastrado.")
        return

    print("\nNomes cadastrados:")
    for indice, nome in enumerate(nomes, start=1):
        print(f"{indice} - {nome}")

while True:
    print("\nMENU")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar todos")
    print("Qualquer outra opção - Encerrar")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        if nome:
            nomes.append(nome)
            print("Nome cadastrado com sucesso.")
        else:
            print("Nome não cadastrado: valor vazio.")

    elif opcao == "2":
        listar()
        if nomes:
            try:
                indice = int(input("Digite o número do cadastro que deseja atualizar: ")) - 1
                if 0 <= indice < len(nomes):
                    novo_nome = input("Digite o novo nome: ").strip()
                    if novo_nome:
                        nomes[indice] = novo_nome
                        print("Nome atualizado com sucesso.")
                    else:
                        print("Atualização cancelada: nome vazio.")
                else:
                    print("Cadastro não encontrado.")
            except ValueError:
                print("Entrada inválida.")

    elif opcao == "3":
        listar()
        if nomes:
            try:
                indice = int(input("Digite o número do cadastro que deseja excluir: ")) - 1
                if 0 <= indice < len(nomes):
                    removido = nomes.pop(indice)
                    print(f"{removido} foi excluído com sucesso.")
                else:
                    print("Cadastro não encontrado.")
            except ValueError:
                print("Entrada inválida.")

    elif opcao == "4":
        listar()

    else:
        print("Opção não reconhecida. Aplicativo encerrado.")
        break

    continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if continuar != "s":
        print("Aplicativo encerrado.")
        break
