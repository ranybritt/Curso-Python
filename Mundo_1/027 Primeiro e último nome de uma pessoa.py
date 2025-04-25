''' Exercício Python 27: 
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
	Resolução:
'''
n = str(input('Nome completo: ')).strip()
nome = n.split()
print(f'Primeiro nome: {nome[0]}\nSegundo nome: {nome[-1]}')
