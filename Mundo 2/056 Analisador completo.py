'''Exercício Python 56: 
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
	Resolução:
'''
somaidd = 0
maior = 0
velho = ''
menos20 = 0
for p in range(1, 5):
    print(f'------- {p}° pessoa -------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidd += idade
    if sexo in 'Mm' and idade > maior:
        velho = nome
        maior = idade
    if sexo in 'Ff' and idade < 20:
        menos20 += 1
mediaidd = somaidd / 4
print(f'\nA média da idade do grupo é {mediaidd:.1f} anos')
print(f'O homem mais velho do grupo é {velho} com {maior} anos.')
print(f'Total de mulheres com menos de 20 anos: {menos20}')