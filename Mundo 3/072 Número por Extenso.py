'''Exercício Python 072:
Crie um programa que tenha uma dupla totalmente preenchida com uma 
contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) 
e mostrá-lo por extenso.
	Resolução:
'''
extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez",
         "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte" )
while True:
    n = int(input("Digite um número de 0 a 20: "))
    if 0 <= n <= 20:
        break
    print("Valor inválido. Tente novamente")
print(f"Você digitou o número {extenso[n]}.")
