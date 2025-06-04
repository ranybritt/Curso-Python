'''Exercício Python 58: 
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora 
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
	Resolução:
'''
from random import randint
print('\033[0;35mSeja bem vindo ao Jogo de adivinhação.\033[m')
print('-'*39)
num = int(input('Adivinha qual número inteiro o jogo escolheu: '))
pc = randint(0,10) 
palpite = 1 
while pc != num:
    print('\033[0;31mVocê não acertou!\033[m')
    num = int(input('Digite um número inteiro novamente: '))
    palpite += 1
print(f'\033[0;32mVocê acertou com {palpite} tentativas!\033[m')
