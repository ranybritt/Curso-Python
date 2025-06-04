''' Exercício Python 62: 
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
    Resolução:
'''
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ➝  ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Deseja mostrar quantos termos a mais: '))
print(f'A progressão aritmética teve {total} termos.')
