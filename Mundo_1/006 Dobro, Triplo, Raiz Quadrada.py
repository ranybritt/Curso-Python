''' 
Exercício Python 006: 
Crie um algoritmo que leia um número e 
mostre o seu dobro, triplo e raiz quadrada.
	Resolução:
'''
n = int(input('Digite um número inteiro: '))
d = n*2
t = n*3
r = n**0.5

print(f'Analisando o número {n} podemos afirmar que: ')
print(f'O dobro é {d}.\nO triplo é {t}.' )
print(f'A raiz quadrada é {r:.2f}.')
