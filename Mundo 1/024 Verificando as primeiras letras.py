''' Exercício Python 24: 
Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome “SANTO”.
	Resolução:
'''
cidade = str(input('Digite o nome da cidade: ')).strip()
print(f'A cidade começa com o nome "SANTO"? {"SANTO" in cidade[:5].upper()}')   