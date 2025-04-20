from random import choice
print('Quem será o escolhido da vez?')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print(f'O aluno sorteado foi {sorteio}')
