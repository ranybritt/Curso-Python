''' 
Exercício Python 7: 
Desenvolva um programa que leia as duas notas de um aluno, 
calcule e mostre a sua média.
	Resolução:
'''
aluno = str(input('Digite o nome do aluno: '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

print(f'A media do aluno(a) {aluno} é {m:.2f}')
