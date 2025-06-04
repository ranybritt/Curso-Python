'''Exercício Python 65: 
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
	Resolução:
'''
n = soma = media = maior = menor = 0
resp = 'S'
cont = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]
media = soma / cont
print(f'A quantidade de números foi {cont}\nA soma é {soma}')
print(f'A média é {media:.2}')
print(f'O número maior é {maior} e o menor é {menor}')

