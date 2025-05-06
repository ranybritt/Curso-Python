''' Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será
formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
	Resolução:
'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1==r2==r3:
        print('É uma trângulo EQUILÁTERO.')
    elif r1==r2!=r3 or r3==r1!=r2 or r3==r2!=r1:
        print('É um triângulo ISÓSCELES.')
    else: 
        print('É um triângulo ESCALENO.')
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')

