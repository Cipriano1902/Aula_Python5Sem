from aluno import Aluno

class ServicoAlunos:
    def __init__(self):
        self._alunos = {}
        self._proxima_matricula = 1

    def _gerar_matricula(self):
        matricula = f"ALU{self._proxima_matricula:05d}"
        self._proxima_matricula += 1
        return matricula

    def cadastrar(self, nome, email, data_nascimento):
        matricula = self._gerar_matricula()
        aluno = Aluno(
            matricula=matricula,
            nome=nome,
            email=email,
            data_nascimento=data_nascimento,
        )
        self._alunos[matricula] = aluno
        return aluno

    def buscar(self, matricula):
        return self._alunos.get(matricula.strip().upper())

    def remover(self, matricula):
        return self._alunos.pop(matricula.strip().upper(), None)

    def listar(self):
        return list(self._alunos.values())

    def atualizar(self, matricula, nome=None, email=None, data_nascimento=None):
        aluno = self.buscar(matricula)
        if aluno is None:
            return None

        if nome is not None:
            aluno.nome = nome
        if email is not None:
            aluno.email = email
        if data_nascimento is not None:
            aluno.data_nascimento = data_nascimento

        return aluno
