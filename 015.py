print(' Aluguel de Carros ')
print('-' * 20)
nome = str(input('Nome do cliente: '))
kmperc = int(input('Quantidade de quilometros percorridos: '))
dias = int(input('Quantos dias foi alugado: '))
km = kmperc * 0.15
d = dias * 60
print(f'O valor total que o cliente {nome} deverá pagar é {d+km} reais. ')