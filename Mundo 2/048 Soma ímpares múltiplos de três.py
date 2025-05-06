'''Exercício Python 48: 
Faça um programa que calcule a soma entre todos os números que são
múltiplos de três e que se encontram no intervalo de 1 até 500.
	Resolução:
'''
soma = 0
count =0
for cont in range (1, 501, 2):
    if cont % 3 == 0:
        count = count+1
        soma += cont
print(f"A soma de todos os {count} valores acumulados é {soma}.")
