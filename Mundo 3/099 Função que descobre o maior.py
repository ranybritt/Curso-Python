'''Exercício Python 099: 
Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. Seu programa 
tem que analisar todos os valores e dizer qual deles é o maior.
	Resolução:
'''
def maior(* n):
    maior = 0
    for valor in n:
        print(f'{valor}', end=' ')
    print(f'\nForam informados {len(n)} valores.')
    if len(n) > 0:
        maior = n[0]
        for valor in n:
            if valor > maior:
                maior = valor
        print(f'O maior valor é {maior}.')
    else:
        print('Nenhum valor foi informado.')


maior(4,7,2,5,9,1)
maior(65, 98, 14, 77, 45)
maior(2)
