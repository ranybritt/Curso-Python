''' Exercício Python 26: 
Faça um programa que leia uma frase pelo teclado e 
mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e 
em que posição ela aparece a última vez.
	Resolução:
'''
frase = str(input('Digite: ')).upper()
print(f'Informação sobre a frase:\nQuantidade da letra A: {frase.count("A")}')
print(f'A letra A aparece a primeira vez em: {frase.find("A")+1}')
print(f'A letra A aparece a ultima vez em: {frase.rfind("A")+1}')
