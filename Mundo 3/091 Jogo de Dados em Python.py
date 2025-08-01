'''Exercício Python 091: 
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.
	Resolução:
'''
from random import randint
from operator import itemgetter
print('-'*40)
print(f"{'Jogo do maior número':^40}")
print('-'*40)
dados = {'jogador1':randint(1,6),
         'jogador2':randint(1,6),
         'jogador3':randint(1,6),
         'jogador4':randint(1,6)}
ranking = dict()
print('Valores sorteados:')
for k, v in dados.items():
    print(f'O {k} tirou {v}')
ranking = sorted(dados.items(), key= itemgetter(1), reverse=True )
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
