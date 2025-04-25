''' Exercício Python 34: 
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a 
R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Qual o valor do seu sálario: '))
if salario > 1250.00:
    new = salario + (salario * 10 / 100)
    print(f'O seu salário com o aumento de 10% é R${new}')
else:
    ns = salario + (salario* 15 / 100)
    print(f'o seu sálario com o aumento de 15% é R${ns}')
