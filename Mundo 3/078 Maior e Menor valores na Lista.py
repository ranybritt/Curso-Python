'''Exercício Python 078: 
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
	Resolução:
'''
lista=[]
for i in range(0,5):
    lista.append(int(input(f"Digite um  valor para a Posição {i}: ")))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista [i]
print(f"Você digitou os números {lista}")
print(f"O maior número é {maior} está localizando nas posições:  ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i} ", end="")
print(f"\nO menor número é {menor} está localizando nas posições: ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i} ", end="")
