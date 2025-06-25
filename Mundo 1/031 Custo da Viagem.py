''' Exercício Python 31: 
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas.
	Resolução:
'''
distancia = float(input('Distância da viagem em km: '))
if distancia <= 200:
    preço =  distancia*0.50
else:
    preço = distancia*0.45
print(f'O preço da sua passagem vai ser {preço}reais.')
