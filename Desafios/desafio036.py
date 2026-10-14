# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valHouse = float(input('Qual o valor da casa? '))
valSal = float(input('Qual o valor do salário? '))
qntYears = int(input('Em quantos anos você deseja pagar a casa? '))

qntPrestacao = valHouse / (qntYears * 12)

if qntPrestacao > (valSal * 0.3):
    print('Empréstimo negado! O valor da Prestação supera 30% do Salário! O Valor da Prestação é R${:.2f}! 30% do Salário é {}'.format(qntPrestacao, (valSal * 0.3)))
elif qntPrestacao <= (valSal * 0.3):
    print('Empréstimo aprovado! O Valor da Prestação é R${:.2f}'.format(qntPrestacao))
else:
    print('Ocorreu um erro!')
