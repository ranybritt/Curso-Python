'''Exercício Python 081:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
	Resolução:
'''
lista = []
cont = 0
while True:
    n = int(input("Digite o valor: "))
    lista.append(n)
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("-=" * 30)
print(f"Você digitou {len(lista)} números.")
lista.sort(reverse=True)
print(f"A ordem da lista decrescente {lista}")
if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O valor 5 não está na lista")
