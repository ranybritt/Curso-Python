'''Exercício Python 076: 
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
	Resolução:
'''
prod = ("Lápis", 1.75,
        "Borracha", 2.00,
        "Caneta", 3.25,
        "Corretivo", 7.00,
        "Estojo", 15.00,
        "Canetão", 7.00)
print("-"*40)
print(f'{"Listagem de produto":^40}')
print("-"*40)
for pos in range(0, len(prod)):
    if pos % 2 == 0:
        print(f"{prod[pos]:.<30}", end="")
    else:
        print(f"R$ {prod[pos]:>7.2f}")
print("-"*40)
