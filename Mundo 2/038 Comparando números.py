''' Exercício Python 038:
Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
	Resolução:
'''
n1 = int(input('Digite o primeiro número? '))
n2 = int(input('Digite o segundo número? '))

if n1>n2: 
    print(f'O primeiro número ({n1}) é maior.')
elif n1<n2:
    print(f'O segundo número ({n2}) é maior.')
else:
    print('os dois números são iguais.')
