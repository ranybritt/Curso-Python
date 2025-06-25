''' 
Exercício Python 3: 
Crie um programa que leia dois números e mostre a soma entre eles.
	Resolução:
'''
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
soma = n1+n2
#print('A soma do numero', n1, 'e', n2 ,'é', soma)
print('A soma do numero {} e {} é {}'.format(n1, n2, soma))
