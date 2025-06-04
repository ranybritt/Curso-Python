'''Exercício Python 64: 
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando 
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
	Resolução:
'''
s = 0
cont = 0
while True:
    n = int(input('Digite o número inteiro (Digite 999 para parar): '))
    if n == 999:
        break
    s = s + n 
    cont+= 1
print(f'O resultados da soma dos {cont} números é {s}')
    