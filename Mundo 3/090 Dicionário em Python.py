'''Exercício Python 090: 
Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
	Resolução:
'''
dados = dict()
dados['nome'] = str(input("Nome do aluno: "))
dados['media'] = float(input("Média do aluno: "))
if dados['media'] >=  7:
    dados['situação'] = 'APROVADO'
elif 5>= dados['media'] < 7: 
    dados['situação'] = 'Recuperação'
else: 
    dados['situação'] = 'Reprovado'
print('-'*40)
print(f"{'Boletim Escolar':^40}")
print('-'*40)
for k, v in dados.items():
    print(f'   {k}: {v}')
