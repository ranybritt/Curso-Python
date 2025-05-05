'''Exercício Python 44: 
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
	Resolução:
'''
prod = float(input('Valor do produto: R$'))
print('''Forma do pagamento:
[ 1 ] Á vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')

opcao = int(input('Qual das opçôes será? '))

if opcao == 1:
    total = prod -(prod * 10 / 100)
    print('A forma de pagamento é à vista dinheiro/cheque.')
elif opcao == 2:
    total = prod - (prod * 5 / 100)
    print('A forma de pagamento é à vista no cartão.')
elif opcao == 3:
    total = prod
    parc = total / 2
    print('A forma de pagamento é 2x no cartão sem juros.')
    print(f'O valor das parcelas R${parc}')
elif opcao == 4:
    parcela = int(input('Quantas vezes no cartão? '))
    if parcela < 3:
        print('ERRO: Parcelamento deve ser de 3x ou mais.')
        total = 0
    else:
        total = prod + (prod * 20 / 100)
        parc = total / parcela
        print(f'Pagamento em {parcela}x com juros de 20%.')
        print(f'O valor das parcelas será R${parc:.2f}')
else:
    print('Opção inválida.')
    total = 0
print(f'Valor total: R${total:.2f}')