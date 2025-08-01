''' Exercício Python 093: 
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.
	Resolução:
'''
dados = dict()
gols = list()
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input('Partidas jogadas: '))
for p in range(dados['partidas']):
    gol = int(input(f'Quantos gols ele fez na partida {p + 1}? '))
    gols.append(gol)
dados['gols'] = gols
dados['total'] = sum(gols)
print('-'*30)
print(f"O jogador {dados['nome']} jogou {dados['partidas']} partidas.")
for i, g in enumerate(dados['gols']):
    print(f"  => Na partida {i + 1}, fez {g} gols.")
print(f"Foi um total de {dados['total']} gols.")