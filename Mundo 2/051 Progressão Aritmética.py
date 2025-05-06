'''Exercício Python 51: 
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
	Resolução:
'''
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo, razao):
    print(f'{c}', end=', ')

