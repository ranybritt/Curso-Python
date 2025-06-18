'''Exercício Python 67: 
Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
	Resolução:
'''
while True:
    n = int(input('Digite um número? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('Programa finalizado!')
