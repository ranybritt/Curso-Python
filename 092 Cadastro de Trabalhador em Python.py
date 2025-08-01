''' Exercício Python 092: 
Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá 
também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar.
	Resolução:
'''
dados = dict()
while True:
    dados['nome'] = str(input('Digite o nome: '))
    dados['ano'] = int(input('Digite o ano do nascimento: '))
    dados['CTPS'] = int(input('Digite o código da CTPS: '))
    dados['idade'] = 2025 - dados['ano']
    if dados['CTPS'] != 0:
        dados['contratacao'] = int(input('Qual é o ano da contratação: '))
        dados['salario'] = float(input('Valor do sálario: '))
        dados['aposentadoria'] = (dados['contratacao'] + 35) - dados['ano']
    break
print('-' * 40)
for k, v in dados.items():
    print(f'{k.capitalize()}: {v}')
