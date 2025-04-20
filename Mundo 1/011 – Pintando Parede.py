print('Seja bem vindo(a) a calculadora de tinta')
print('Obs: Precisamos dos dados em metros.')

l = float(input('Digite a largura em metros: '))
h = float(input('Digite a altura em metros: '))
a = l * h
tinta = a / 2

print(f'A área da parede é {a}m²')
print(f'Será usado {tinta} litro(s) de tinta para pinta-la.')