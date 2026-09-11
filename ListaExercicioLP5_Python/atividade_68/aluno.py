from dataclasses import dataclass

@dataclass
class Aluno:
    matricula: str
    nome: str
    email: str
    data_nascimento: str
