''' Exercício Python 15:
Escreva um programa que pergunte a quantidade de Km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi 
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado.
    Resolução:
'''
print(' Aluguel de Carros ')
print('-' * 20)
nome = str(input('Nome do cliente: '))
kmperc = int(input('Quantidade de quilometros percorridos: '))
dias = int(input('Quantos dias foi alugado: '))
km = kmperc * 0.15
d = dias * 60
print(f'O valor total que o cliente {nome} deverá pagar é {d+km} reais. ')