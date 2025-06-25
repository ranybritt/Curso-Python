''' 
Exercício Python 11:
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
    Resolução:
'''
print('Seja bem vindo(a) a calculadora de tinta')
print('Obs: Precisamos dos dados em metros.')

l = float(input('Digite a largura em metros: '))
h = float(input('Digite a altura em metros: '))
a = l * h
tinta = a / 2

print(f'A área da parede é {a}m²')
print(f'Será usado {tinta} litro(s) de tinta para pinta-la.')