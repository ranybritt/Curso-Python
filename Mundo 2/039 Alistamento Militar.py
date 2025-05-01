''' Exercício Python 39: 
Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
	Resolução:
'''

from datetime import date 
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc

if idade == 18: 
    print('Você deve se alistar imediatamente.')
elif idade < 18:
    print(f'Você ainda não pode se alistar. No ano de {atual-(idade - 18)} você pode se alistar')
else:
    print(f'Você deveria ter se alistado no ano {atual - (idade - 18)}.')


