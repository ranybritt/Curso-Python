'''Exercício Python 50: 
Desenvolva um programa que leia seis números inteiros e mostre a soma 
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
	Resolução:
'''
soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o número:'))
    if num %2 == 0:
        soma += num
        cont +=1
print(f'A soma dos {cont} números pares é {soma}.')
