'''Exercício Python 16:
Crie um programa que leia um número Real qualquer 
pelo teclado e mostre na tela a sua porção Inteira.
    Resolução:
'''
from math import trunc
num = float(input('Digite um número real: '))
print(f'A porção inteira do número {num} é {trunc(num)}')
