'''Exercício Python 083: 
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
	Resolução:
'''
exp = str(input("Digite a expressão? "))
pilha = []
for símb in exp:
    if símb == "(":
        pilha.append("(")
    elif símb ==(")"):
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão é valida!")
else:
    print("Sua expressão é inválida!")
