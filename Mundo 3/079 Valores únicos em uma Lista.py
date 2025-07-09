'''Exercício Python 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
	Resolução:
'''
números = list()
while True:
    n = int(input("Digite um número: "))
    if n not in números:
        números.append(n)
        print("Valor adicionado!")
    else: 
        print("Valor não adicionado, pois já existe na lista.")
    resp = " "
    while resp not in "SN":
        resp = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break 
números.sort()
print(f"Os números da lista são: {números} ")
