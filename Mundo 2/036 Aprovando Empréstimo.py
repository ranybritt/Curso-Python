''' Exercício Python 36:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
	Resolução:
'''
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu sálario? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
limite = salario * 30 / 100
if prestacao <= limite:
    print('Parabéns! Seu empréstimo foi aprovado.')
else:
    print('Seu empréstimo foi NEGADO.A prestação excede 30% do seu salário.')
