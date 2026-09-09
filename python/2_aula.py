# Variáveis:

nome = 'Josue'
idade = 46
altura = 1.80
vivo = True
nascimento = '1980-02-19'

# Verificar conteúdo das variáveis:

print(nome)
print(idade)
print(altura)
print(vivo)
print(nascimento)

# Concatenando informações:

print('Meu nome é:', nome )
print('Minha idade é:', idade )
print(f'Minha altura é: altura você nasceu em: {nascimento}')

# Verificando o tipo das variáveis:

print(f'A variável nome é do tipo: {type(nome)}')
print(type(idade))
print(type(altura))
print(type(vivo))
print(type(nascimento))

# Exemplo de uso dos métodos de uma classe:

print(f'Conteúdo original: {nome}')
print(f'Conteúdo em maiúsculo: {nome.upper()}')
print(f'Conteúdo capitalize: {nome.capitalize()}')
