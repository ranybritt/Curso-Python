'''Exercício Python 095: 
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
	Resolução:
'''
jogadores = []
while True:
	dados = dict()
	gols = []
	dados['nome'] = str(input('Nome do jogador: '))
	dados['partidas'] = int(input('Partidas jogadas: '))
	for p in range(dados['partidas']):
		gols.append(int(input(f'Quantos gols ele fez na partida {p + 1}? ')))
	dados['gols'] = gols[:]
	dados['total'] = sum(gols)
	jogadores.append(dados.copy())
	resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
	while resp not in 'SN':
		resp = str(input('Resposta inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('-' * 40)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<20}{"Total":<5}')
print('-' * 40)
for i, j in enumerate(jogadores):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<20}{j["total"]:<5}')
while True:
    print('-' * 40)
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f'   No jogo {i + 1} fez {g} gols.')
