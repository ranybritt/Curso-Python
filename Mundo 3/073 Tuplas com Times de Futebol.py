'''Exercício Python 73: 
Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Vasco Gama.
	Resolução:
'''
camp = ("Flamengo", "Cruzeiro", "Red Bull Bragantino SP", "Palmeiras SP", "Bahia", "Fluminense RJ", "Atletico Mineiro MG",
        "Botafogo FR RJ", "Mirassol FC", "Corinthians SP", "Gremio", "Ceará SC CE", "Vasco Gama", "São Paulo FC SP",
        "Santos FC SP", "EC Vitória BA", "Internacional RS", "Fortaleza CE", "EC Juventude RS", "Recife")
print("\033[0;31mInformação da tabela do Campeonato Brasileiro de Futebol 2025\033[m")
print(f"Lista de times no Brasilerão: {camp}\n")
print(f"Os 5 primeiros times na colocação é {camp[:4]}.\n")
print(f"Os últimos 4 colocados é {camp[-4:]}\n")
print(f"Os times em ordem alfabética{sorted(camp)}\n")
print(f"O time Vasco da gama está localizado na posição {camp.index('Vasco Gama')+1}°\n")
while True:
    onde = str(input("Qual time você deseja saber a posição: ")).strip().lower()
    encont = [time for time in camp if onde in time.lower()]
    if encont:
        for onde in encont:
            print(f"O time {onde} está na {camp.index(onde)+1}° posição.")
        break
    else:
        print("Eita! Seu time não foi encontrado na tabela.")
        print("Provavelmente ele não foi selecionado ou a digitação está errada.")
