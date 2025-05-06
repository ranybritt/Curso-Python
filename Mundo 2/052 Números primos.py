'''Exercício Python 52: 
Faça um programa que leia um número inteiro e
diga se ele é ou não um número primo.
	Resolução:
'''
num = int (input('Digite o número: '))
tot = 0
for c in range (1, num +1):
    if num % c == 0:
        print(f'\033[33m', end=' ')
        tot += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('Ele é PRIMO!')
else:
    print('Ele é NÃO É PRIMO!')
    