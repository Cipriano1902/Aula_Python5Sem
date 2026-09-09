fruta = 'Uva'

frutas = ['Maça', 'Laranja', 'Morango', 'Kiwi']

# prontando cada fruta individual

print(frutas[2])

# printando lista completa

for fruta in frutas:
    print(fruta)



# Lista com enumeração

alunos = ['victor' , 'Josue', 'Nice', 'Ewerton', 'Eloi']

for indice, aluno in enumerate(alunos):
    print(indice, aluno)
    if indice == 2:
        print(f'A aluna {aluno} é esforçada!')