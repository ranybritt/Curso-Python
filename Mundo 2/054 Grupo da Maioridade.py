'''Exercício Python 54: 
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a 
maioridade e quantas já são maiores.
	Resolução:
'''
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for pessoa in range(1,8):
    nasc = int(input('Digite o ano de nascimento: '))
    calculo = ano - nasc 
    if calculo >= 18:
        maior += 1
    else: 
        menor += 1
print(f'Existe {maior} pessoas maiores de idade e {menor} menores de idade.')
