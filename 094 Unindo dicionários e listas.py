'''Exercício Python 094:
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
	Resolução:
'''
pessoas=[]
soma = media = 0
while True:
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    while dados['sexo'] not in 'FM':
        dados['sexo'] = str(input('Sexo inválido. Digite [F/M]: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Resposta inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
media = soma / len(pessoas)
print('-'*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média das idades são {media:.2f}')
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
print(f'Mulheres cadastradas: {mulheres}')
print('Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print(f"   Nome: {p['nome']}, Idade: {p['idade']}, Sexo: {p['sexo']}")
