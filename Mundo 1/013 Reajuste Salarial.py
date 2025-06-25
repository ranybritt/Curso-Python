''' Exercício Python 13:
Faça um algoritmo que leia o salário de um funcionário.
Mostre seu novo salário, com 15% de aumento.
    Resolução:
'''
s = float(input('Digite seu sálario: '))
aum = s + (s * 15 / 100)
print(f'O seu sálario com o aumento de 15% corresponde a R${aum} ')
