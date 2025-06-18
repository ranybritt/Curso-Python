'''Exercício Python 66:
Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre elas (desconsiderando o flag).
	Resolução:
'''
s = 0
cont = 0
while True:
    n = int(input('Digite um número inteiro? '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} números.')
print(f'A soma entre eles é {s}.')
