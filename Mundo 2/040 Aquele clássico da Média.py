''' Exercício Python 040: 
Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
	Resolução:
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print(f'A média final é {média:.2f}')
if média >= 7.0:
    print(f'APROVADO! O aluno atingiu a média.')
elif 5.0 <= média < 7.0:
    print(f'RECUPERAÇÃO! Deverá fazer novamente a prova.')
else: 
    print(f'REPROVADO! O aluno não atingiu a média.')
