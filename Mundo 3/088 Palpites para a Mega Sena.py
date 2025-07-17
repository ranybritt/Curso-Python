'''Exercício Python 088: 
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados 
e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
	Resolução:
'''
from random import randint

jogos = list()
print("-"*30)
print("     Sorteio da Mega Sena     ")
print("-"*30)
quant = int(input("Quantos jogos deseja sortear: "))
for c in range(0, quant):
    lista = []
    while len(lista) < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos.append(lista)
print("-"*30)
print(f"SORTEANDO {quant} JOGOS")
print("-"*30)
for i, l in enumerate(jogos, 1):
    print(f"Jogo {i}: {l}")
