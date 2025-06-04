'''Exercício Python 060: 
Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
	Resolução:
'''
num = int(input('Digite um número: '))
fact = num
resul = 1
print(f'Calculando {num}! = ', end='')
while fact > 0:
    print(f'{fact}', end='')
    print(' x ' if fact > 1 else ' = ', end='')
    resul *= fact
    fact -= 1
print(f'\033[0;32m{resul}\033[m')
