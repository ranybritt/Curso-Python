'''Exercício Python 071: 
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
	Resolução:
'''
valor = int(input("Qual o valor que deseja sacar? "))
total = valor
cédula = 50
totcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        totcéd += 1
    else:
        if totcéd > 0:
            print(f"Sacou {totcéd} cédula(s) de R${cédula}")
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totcéd = 0
        if total == 0:
            break
print("Fim do programa")