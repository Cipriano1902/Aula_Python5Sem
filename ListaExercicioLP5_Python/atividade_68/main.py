from servico_alunos import ServicoAlunos
from validacoes import validar_nome, validar_email, validar_data_nascimento

servico = ServicoAlunos()

def ler_nome():
    while True:
        try:
            return validar_nome(input("Nome: "))
        except ValueError as erro:
            print(erro)

def ler_email():
    while True:
        try:
            return validar_email(input("E-mail: "))
        except ValueError as erro:
            print(erro)

def ler_data():
    while True:
        try:
            return validar_data_nascimento(input("Data de nascimento (DD/MM/AAAA): "))
        except ValueError as erro:
            print(erro)

def mostrar_aluno(aluno):
    print("-" * 40)
    print(f"Matrícula: {aluno.matricula}")
    print(f"Nome: {aluno.nome}")
    print(f"E-mail: {aluno.email}")
    print(f"Data de nascimento: {aluno.data_nascimento}")

def cadastrar():
    aluno = servico.cadastrar(
        nome=ler_nome(),
        email=ler_email(),
        data_nascimento=ler_data(),
    )
    print(f"Aluno cadastrado com sucesso. Matrícula: {aluno.matricula}")

def atualizar():
    matricula = input("Matrícula do aluno: ").strip().upper()
    aluno = servico.buscar(matricula)

    if aluno is None:
        print("Matrícula não encontrada.")
        return

    print("Deixe o campo vazio para manter o valor atual.")

    nome_digitado = input(f"Nome [{aluno.nome}]: ").strip()
    email_digitado = input(f"E-mail [{aluno.email}]: ").strip()
    data_digitada = input(
        f"Data de nascimento [{aluno.data_nascimento}]: "
    ).strip()

    try:
        nome = validar_nome(nome_digitado) if nome_digitado else None
        email = validar_email(email_digitado) if email_digitado else None
        data = validar_data_nascimento(data_digitada) if data_digitada else None
    except ValueError as erro:
        print(f"Atualização cancelada: {erro}")
        return

    servico.atualizar(matricula, nome, email, data)
    print("Aluno atualizado com sucesso.")

def remover():
    matricula = input("Matrícula do aluno: ").strip().upper()
    removido = servico.remover(matricula)

    if removido is None:
        print("Matrícula não encontrada.")
    else:
        print(f"Aluno {removido.nome} removido com sucesso.")

def listar():
    alunos = servico.listar()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        mostrar_aluno(aluno)
    print("-" * 40)

def buscar():
    matricula = input("Matrícula do aluno: ").strip().upper()
    aluno = servico.buscar(matricula)

    if aluno is None:
        print("Matrícula não encontrada.")
    else:
        mostrar_aluno(aluno)
        print("-" * 40)

def main():
    while True:
        print("\nSISTEMA DE CADASTRO DE ALUNOS")
        print("1 - Cadastrar aluno")
        print("2 - Atualizar aluno")
        print("3 - Remover aluno")
        print("4 - Listar todos")
        print("5 - Mostrar aluno por matrícula")
        print("0 - Sair")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            atualizar()
        elif opcao == "3":
            remover()
        elif opcao == "4":
            listar()
        elif opcao == "5":
            buscar()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
