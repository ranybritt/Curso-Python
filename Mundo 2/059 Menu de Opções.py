''' Exercício Python 059:
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
	Resolução:
'''
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opc = 0 
while opc != 5:
    print('De acordo com o menu. ')
    print('\033[0;33m[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\033[m')
    print('\033[0;33m[ 4 ] novos números\n[ 5 ] sair do programa\033[m')
    opc = int (input('Selecione o que deseja fazer os valores: '))
    if opc == 1:
        soma = n1 + n2 
        print(f'A resultado da soma é \033[0;32m{soma:.2f}\033[m')
    elif opc == 2:
        mult = n1 * n2
        print(f'A resultado da multiplicação é \033[0;32m{mult:.2f}\033[m')
    elif opc == 3:
        if n1 > n2:
            print(f'O número maior é \033[0;32m{n1}\033[m')
        elif n2 > n1: 
            print(f'O número maior é \033[0;32m{n2}\033[m')
        else:
            print(f'Os números são iguais')
    elif opc == 4: 
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif opc == 5:
        print('\033[0;31mSaindo do programa...\033[m')
    else:
        print('\033[0;31mOpção inválida! Tente novamente.\033[m')
print('Fim')
