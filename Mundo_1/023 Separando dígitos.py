''' Exercício Python 23: 
Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.
	Resolução:
'''
print('Separador de dígitos')
print('-' * 30)
num = int(input('Digite um número: '))
n = str(num).zfill(4)
print(f'O número {num} separado é: ')
print(f'Unidade: {n[3]}\nDezena: {n[2]}')
print(f'Centena: {n[1]}\nMilhar: {n[0]}')
