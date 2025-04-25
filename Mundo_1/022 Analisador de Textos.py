''' Exercício Python 22:
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
Resolução:
'''

nome = str(input('Nome completo: ')).strip()

print('Analisando o nome...')
print(f'Nome com todas as letras maiúscula: {nome.upper()}')
print(f'Nome com todas as letras minúscula: {nome.lower()}')
print(f'Quantidade de letras no nome todo: {len(nome.replace(" ", ""))}')
print(f'Quantidade de letras no primeiro nome: {len(nome.split()[0])}')