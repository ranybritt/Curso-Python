'''Exercício Python 61: 
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando 
os 10 primeiros termos da progressão usando a estrutura while.
	Resolução:
'''
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}➝ ', end='')
    termo += razao
    cont += 1
print('FIM')
