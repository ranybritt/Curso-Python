'''Exercício Python 53: 
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, 
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
	Resolução:
'''
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else: 
    print('A frase não é um palíndromo!')
