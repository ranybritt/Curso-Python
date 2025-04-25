''' Exercício Python 30:
Crie um programa que leia um número inteiro e 
mostre na tela se ele é PAR ou ÍMPAR.
	Resolução:
'''
num = int(input('Digite um número para descobrir se ele é ímpar ou par: '))
n = num % 2
if n==0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')