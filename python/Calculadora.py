print('Escolha a operação desejada:')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = int(input('Escolha a operação desejada: '))
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

match opcao:            
    case 1:
        print(f'a soma é {numero1 + numero2}')
    case 2:
        print(f'A subtração é {numero1 - numero2}')
    case 3:
        print(f'A multiplicação é {numero1 * numero2}')  
    case 4:
        print(f'A divisão é {numero1 / numero2}')
    case _:
        print('Opção inválida!')