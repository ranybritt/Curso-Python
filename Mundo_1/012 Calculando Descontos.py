''' 
Exercício Python 12:
Faça um algoritmo que leia o preço de um produto.
Mostre seu novo preço, com 5% de desconto.
    Resolução:
'''
print('Calculadora de desconto:')
p = float(input('Preço do produto: R$'))
pn = p - (p * 5 / 100)
print(f'O preço original do produto: R${p}')
print(f'O preço com 5% desconto: R${pn:.2f}')
