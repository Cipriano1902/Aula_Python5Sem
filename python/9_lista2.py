# Manipular lista # sempre usar for para printar

cavaleiros = ['seya', 'shun', 'chiryu','yoga']

for cavaleiro in cavaleiros:
    print(cavaleiro)

# acrescentando iten na lista(cavaleiros)

cavaleiros.append ('ikke')

for cavaleiro in cavaleiros:
    print(cavaleiro)


# acresncentar varios itens na lista

cavaleiros.extend ({'Marin', 'shina'})
print(cavaleiros)


# acrescentando item em posiçao numeral especifica

cavaleiros.insert(0, 'athena')
print(cavaleiros)


## removendo item de uma lista ####
#removendo intem especifico

cavaleiros.pop(0)
print(cavaleiros)

#removendo pelo nome da varialvel

cavaleiros.remove('shina')
print(cavaleiros)


#removendo o ultomo nome
cavaleiros.pop()
print(cavaleiros)


# apagando a lista toda mas não da memoria

# cavaleiros.clear()
# print(cavaleiros)


# ecluindo e removando a lista da memoria
# del cavaleiros
# print(cavaleiros)



# organizando lista

cavaleiros.sort()  # ordem alfabetica
print(cavaleiros)

cavaleiros.reverse() # organiza do menor para o maior
print(cavaleiros)


# verificando o tamnho da lista

print(len(cavaleiros))


# descobrindo o indice de um elemneto na lista

print(cavaleiros.index('seya'))

cavaleiros.pop((cavaleiros.index('seya')))
print(cavaleiros)