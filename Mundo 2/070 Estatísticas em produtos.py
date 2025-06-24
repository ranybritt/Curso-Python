'''Exercício Python 70: 
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
	Resolução:
'''

preco = 0
soma = 0
prodcaro = 0
menor = 0
cont = 0
barato = ""
while True:
    nome = str(input("Nome do prduto: ")).strip()
    preco = float(input("Preço: R$"))
    soma += preco
    cont += 1
    if preco > 1000:
        prodcaro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = " "
    while resp not in "SN":
        resp = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break 
print("            Fim do programa")
print (f"O total da compra é R${soma:.2f}")
print(f"Possui {prodcaro} produto(s) maior(es) que R$1000")
print(f"O produto mais barato é {barato} que custa R${menor}")