'''Exercício Python 085: 
Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
	Resolução:
'''
valores = [[],[]]
impar = par = 0
for i in range(0,7):
    n = int(input("Número: "))
    if n % 2 == 0:
        valores[0].append(n)
    if n % 2 == 1:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print(f"Os números pares são {valores[0]}")
print(f"Os números impares são {valores[1]}")
    