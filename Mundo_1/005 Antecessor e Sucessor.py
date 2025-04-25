''' 
Exercício Python 5: 
Faça um programa que leia um número Inteiro e 
mostre na tela o seu sucessor e seu antecessor.
	Resolução:
'''
print('Olá, seja bem vindo(a)')

n = int(input('Digite um número inteiro: '))
antecessor = n-1
sucessor = n+1
print(f'O antecessor do número {n} é {antecessor}.' )
print(f'O sucessor do número {n} é {sucessor}.')
