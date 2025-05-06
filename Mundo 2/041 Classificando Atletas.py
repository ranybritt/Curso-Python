''' Exercício Python 041: 
A Confederação Nacional de Natação precisa de um programa que leia o ano 
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
	Resolução:
'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano do nascimento do atleta: '))
idade = atual - nasc
if idade <= 9:
    print('O atleta participará da categoria MIRIM.')
elif idade <= 14:
    print('O atleta participará da categoria INFANTIL.')
elif idade <= 19:
    print('O atleta participará da categoria JÚNIOR.')
elif idade <= 25:
    print('O atleta participará da categoria SÊNIOR.')
else:
    print('O atleta participará da categoria MASTER.')
