''' Exercício Python 17: 
Faça um programa que leia o comprimento do cateto oposto, adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
    Resolução:
'''
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print(f'A hipotenusa é {h:.2f}')