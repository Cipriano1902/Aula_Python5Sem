# Lista de Atividades em Python

Esta pasta contém as soluções dos exercícios informados na lista.

## Organização

- `atividade_01.py` até `atividade_67.py`: exercícios individuais.
- `atividade_32_PULAR.txt`: exercício 32 marcado como pulado, conforme solicitado.
- `atividade_68/`: versão modular do cadastro de alunos.
  - `main.py`: menu e interação com o usuário.
  - `aluno.py`: modelo de dados do aluno.
  - `validacoes.py`: validações de nome, e-mail e data.
  - `servico_alunos.py`: regras de cadastro, busca, atualização, remoção e listagem.
- `atividade_69.py`: jogo da velha refatorado, com empate, bloqueio de posição ocupada e opção de nova partida.

## Como executar

Abra o terminal na pasta e use:

```bash
python atividade_01.py
```

Para a atividade 68:

```bash
cd atividade_68
python main.py
```

Para a atividade 69:

```bash
python atividade_69.py
```

## Observações

- Na atividade 13, as estações foram organizadas conforme o hemisfério sul.
- Na atividade 16, os preços dos combustíveis são valores ilustrativos, pois a lista não forneceu preços específicos.
- Na atividade 57, o número secreto foi definido como `7`.
- As entradas mais complexas das atividades 68 e 69 foram validadas para evitar encerramentos inesperados por dados incorretos.
