'''Exercício Python 082: 
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
	Resolução:
'''
numeros = []
pares = []
impares = []
while True:
    n = int(input("Qual é o valor: "))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else: 
        impares.append(n)
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Os números da lista é {numeros}")
print(f"Os números pares são {pares}")
print(f"Os números impares são {impares}")
