''' Exercício Python 28: 
Escreva um programa que faça o computador “pensar” em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido 
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
	Resolução:
'''
from random import randint
from time import sleep
pc = randint(0, 5)
num = int(input('Adivinhe um número inteiro entre 0 a 5 que o computador pensou: '))
print('Processando...')
sleep(2)
if pc==num:
    print(f'Parabéns! Você acertou o número é {pc}')
else:
    print(f'Que pena! você errou, o numero é {pc}\nTente novamente')
