from datetime import datetime
import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validar_nome(nome):
    nome = nome.strip()
    if len(nome) < 2:
        raise ValueError("Nome deve possuir pelo menos 2 caracteres.")
    return nome

def validar_email(email):
    email = email.strip().lower()
    if not EMAIL_RE.match(email):
        raise ValueError("E-mail inválido.")
    return email

def validar_data_nascimento(data):
    data = data.strip()
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError as exc:
        raise ValueError("Data inválida. Use o formato DD/MM/AAAA.") from exc
    return data
