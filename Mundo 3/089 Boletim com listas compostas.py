'''Exercício Python 089:
Crie um programa que leia nome e duas notas de vários alunos e 
guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que 
o usuário possa mostrar as notas de cada aluno individualmente.
	Resolução:
'''
boletim = list()
media = 0
while True:
	nome = str(input("Nome: "))
	nota1 = float(input("Primeira nota: "))
	nota2 = float(input("Segunda nota: "))
	media = (nota1 + nota2) / 2
	boletim.append([nome, [nota1, nota2], media])
	resp = " "
	while resp not in "SN":
		resp = str(input("Deseja adicionar mais um aluno: [S/N]")).strip().upper()[0]
	if resp == "N":
		break
print("-"*40)
print(f"{'Nº.':<4}{'ALUNO':<15}{'MÉDIA':>8}")
print("-"*40)
for i, a in enumerate(boletim):
    print(f"{i:<4}{a[0]:<15}{a[2]:>8.1f}")
while True:
    print("-"*40)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc >= 0 and opc < len(boletim):
        print(f"Notas de {boletim[opc][0]} são: {boletim[opc][1]}")
print("<<< VOLTE SEMPRE >>>")

