''' Exercício Python 29: 
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
	Resolução:
'''
velocidade = float(input('Qual a velocidade atual do carro: '))
if velocidade > 80:
    print('Multado! Você excedeu o limite de velocidade que é 80km/h')
    multa = (velocidade-80) * 7
    print(f'Você deverá pagar a multa de {multa:.2f} R$')
    print('Cuidado! Dirija com segurança.')
else:
    print('Tenha um bom dia. Dirija com segurança.')

