'''Exercício Python 68: 
Faça um programa que jogue par ou ímpar com o computador. O jogo 
só será interrompido quando o jogador perder, mostrando 
o total de vitórias consecutivas que ele conquistou no final do jogo.
	Resolução:
'''    
from random import randint
print('Jogo impar ou par:')
print('-'*25)
cont = 0

while True:
    n = int(input('Digite um número de 1 a 10: '))
    pc = randint(0,10)
    total = n + pc
    esc = ''
    while esc not in 'PI':
        esc = str(input('Você escolhe Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogador jogou {n} e o computador jogou {pc}\nA soma entre eles é {total}')
    if esc == 'P': 
        if total % 2 == 0: 
            cont += 1
            print(f'Parabéns! Você venceu.\n Você possui {cont} vitorias')
        else: 
            print(f' Você perdeu! Fim de jogo.')
            print(f'Total de vitórias consecutivas: {cont}')
            break
    elif esc == 'I':
        if total % 2 == 1:
            cont += 1
            print(f'Parabéns! Você venceu.\n Você possui {cont} vitorias')
        else: 
            print(f' Você perdeu! Fim de jogo.')
            print(f'Total de vitórias consecutivas: {cont}')
            break
