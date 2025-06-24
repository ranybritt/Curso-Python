'''Exercício Python 69: 
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
	Resolução:
'''
idade = 0
totM = 0
totF = 0
maior = 0
while True:
    idade = int(input("Qual a idade? "))
    sexo = " "
    while sexo not in "FM":
        sexo = str(input("Qual o sexo? [F/M] ")).strip().upper()[0]
    if sexo == "M":
        totM += 1
    if sexo == "F" and idade < 20:
        totF += 1
    if idade >= 18:
        maior += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
    
print(f"Há {maior} pessoas maiores de 18 anos.")
print(f"Foram cadastrados {totM} homens.")
print(f"Há {totF} mulheres que tem menos de 20 anos.")