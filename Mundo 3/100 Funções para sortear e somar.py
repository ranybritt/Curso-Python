'''Exercício Python 100: 
Faça um programa que tenha uma lista chamada números e 
duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los 
dentro da lista e a segunda função vai mostrar a soma entre 
todos os valores pares sorteados pela função anterior.
    Resolução:
'''
import random
numeros = list()
def sorteia():
    print('Sorteando 5 valores: ', end='')
    for _ in range(5):
        n = random.randint(0, 10)
        numeros.append(n)
        print(f'{n}', end=' ')
    print('PRONTO!')
def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares temos {soma}')


sorteia()
somaPar()
