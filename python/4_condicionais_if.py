# Condicional IF:

idade = 15
acompanhado = True


# if idade >= 18:
#     print(f'Você é maior de idade! {idade}')
# else:
#     print(f'Você é menor de idade! {idade}')


# if idade >= 18:
#     print('Pode assistir ao filme!')
# elif (idade >= 15) and (acompanhado == True):       
#     print('Você é menor, mas pode assistir ao filme acompanhado!')
# elif (idade >= 15) and (acompanhado == False):
#     print('Você é menor e não pode assistir ao filme desacompanhado!')
# else:
#     print('Você é menor de idade e não pode assistir ao filme!')

if idade >= 18:
    print('Pode assistir ao filme!')
elif idade >= 15:
    if acompanhado == True:
        print('Você é menor, mas pode assistir ao filme acompanhado!')
    else:
        print('Você é menor e não pode assistir ao filme desacompanhado!')    
else:
    print('Você é menor de idade e não pode assistir ao filme!')

