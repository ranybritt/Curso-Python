''' Exercício Python 37: 
Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
	Resolução:
'''
n = int(input('Digite um número inteiro: '))
print('\nEscolha qual será a base da conversão:')
print('=' * 40)
print('1 - Binário\n2 - Octal\n3 - Hexadecimal')
print('=' * 40)
opcao = int(input('Qual base de conversão? '))
print('=' * 40)
if opcao == 1:
    print(f'O número {n} convertido para binário é: {bin(n)[2:]}')
elif opcao == 2:
    print(f'O número {n} convertido para octal é: {oct(n)[2:]}')
elif opcao == 3:
    print(f'O número {n} convertido para hexadecimal é: {hex(n)[2:]}')
else:
    print('Opção inválida.')
    