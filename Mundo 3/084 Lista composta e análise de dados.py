'''Exercício Python 084: 
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
	Resolução:
'''
pessoas = []
maior = menor = 0
while True:
    nome = str(input("Nome: ")).strip()
    peso = float(input("Peso: "))
    pessoas.append([nome, peso])
    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print('-' * 30)
print(f"Foram cadastrados {len(pessoas)} pessoas.")
print(f"O maior peso foi {maior:.2f}Kg. Peso de: ", end="")
for p in pessoas:
    if p[1] == maior: 
        print(f"[{p[0]}] ")
print()
print(f"O menor peso foi {menor:.2f}Kg. Peso de: ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
