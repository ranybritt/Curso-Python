'''Exercício Python 45: 
Crie um programa que faça o computador jogar Jokenpô com você.
	Resolução:
'''
from random import randint
from time import sleep
print('Vamos jogar Jokenpô!')
print('''
-----------------
| [ 0 ] Pedra   |
| [ 1 ] Papel   |
| [ 2 ] Tesoura |
-----------------   
''')
lista = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
player = int(input('Qual você escolhe? '))

print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PÔ!")

print(f'Você escolheu {lista[player]}.')
print(f'O computador escolheu {lista[pc]}.')

if pc == 0:
    if player == 0:
        print('EMPATOU!')
    elif player == 1:
        print('VOCÊ VENCEU!')
    elif player == 2:
        print('VOCÊ PERDEU!')
    else:
        print('DADO INVÁLIDO!')
elif pc == 1:
    if player == 0:
        print('VOCÊ PERDEU!')
    elif player == 1:
        print('EMPATOU!')
    elif player == 2:
        print('VOCÊ GANHOU!')
    else:
        print('DADO INVÁLIDO!')
elif pc == 2:
    if player == 0:
        print('VOCÊ GANHOU!')
    elif player == 1:
        print('VOCÊ PERDEU!')
    elif player == 2:
        print('EMPATOU!')
    else:
        print('DADO INVÁLIDO.')