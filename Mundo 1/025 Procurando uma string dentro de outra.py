'''Exercício Python 25: 
Crie um programa que leia o nome de uma pessoa e 
diga se ela tem “SILVA” no nome.
    Resolução:
'''
nome = str(input('Digite o nome: ')).strip()
print(f'O nome tem "Silva"? {"SILVA" in nome.upper()}')
