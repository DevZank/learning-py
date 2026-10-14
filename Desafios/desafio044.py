# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor do produto? R$'))
opt = int(input('\n[1] - à vista Dinheiro/Cheque\n[2] - à vista no Cartão\n[3] - em até 2x no Cartão\n[4] - 3x ou mais no cartão\nQual o método de Pagamento? '))

if opt == 1:
    valor = valor - valor * 0.1
    print('O valor final do produto é R${}'.format(valor))
elif opt == 2:
    valor = valor - valor * 0.05
    print('O valor final do produto é R${}'.format(valor))
elif opt == 3:
    print('O valor final do produto é R${}'.format(valor))
elif opt == 4:
    valor = valor + valor * 0.20
    print('O valor final do produto é R${}'.format(valor))
else:
    print('Opção não encontrada')