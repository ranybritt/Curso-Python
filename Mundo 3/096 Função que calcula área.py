'''Exercício Python 096:
Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.
	Resolução:
'''
def area(larg,comp):
    a = larg * comp
    print(f'A área é {a:.2f}m².')
    

print('Calculadora de área')
print('-'*30)
l = float(input('Qual é a largura: '))
c = float(input('Qual é o comprimento: '))
area(l,c)
