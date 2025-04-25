''' 
Exercício Python 10: 
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos dólares ela pode comprar.
    Resolução:
'''
print('Seja bem vindo(a) ao nosso cotador de moedas: R$')

n = float(input('Digite o valor em reais: R$'))
dólar = n / 5.86
euro = n / 6.30
libra = n / 7.40
peso = n / 0.025
print(f'Com R${n:.2f}, você pode comprar aproximadamente:')
print(f'Dólar: US${dólar:.2f} \nEuro: €{euro:.2f}')
print(f'Libra: £{libra:.2f}\nPeso: ARS${peso:.2f}')

# Cotação baseada no dia 17/04/2025. Valores podem variar com o tempo