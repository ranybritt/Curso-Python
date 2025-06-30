'''Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado 
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
	Resolução:
'''
num = (int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")))
print(f"Os números digitados foram {num}.")
print(f"O número 9 apareceu {num.count(9)}vezes.")
if 3 in num:
    print(f"O número 3 está na {num.index(3)+1}ª posição.")
else:
    print("O número 3 não está na lista.")
print("Os valores pares digitados é ", end=" ")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
