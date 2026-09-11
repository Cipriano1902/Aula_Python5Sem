# Case:

numero1 = 10
numero2 = 5

opcao = 4

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
       
