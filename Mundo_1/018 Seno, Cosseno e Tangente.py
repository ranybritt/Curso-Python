''' Exercício Python 18: 
Faça um programa que leia um ângulo qualquer.
Mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
    Resolução:
'''
import math
ang = float(input('Digite o ângulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O ângulo {ang} corresponde:\nSeno: {sen:.2f}')
print(f'Cosseno: {cos:.2f}\nTangente: {tan:.2f}')
