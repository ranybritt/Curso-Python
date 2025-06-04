'''Exercício Python 57: 
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
	Resolução:
'''
sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados incorretos!\nDigite o sexo corretamente F ou M: ')).strip().upper()[0]
print(f'Sexo {sexo} registrados com sucesso.')
