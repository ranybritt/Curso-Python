''' 
Exercício Python 4: 
Faça um programa que leia algo pelo teclado e mostre na tela 
o seu tipo primitivo e todas as informações possíveis sobre ele.
	Resolução:
'''
x = input('Digite algo:')
print('O tipo primitivo é', type(x))
print('Há espaço?', x.isspace())
print('É um numéro?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumerico?', x.isalnum())
print('Está em maiusculo?', x.isupper())
print('Está em minusculo?', x.islower())
print('Está capitalisada?', x.istitle())
