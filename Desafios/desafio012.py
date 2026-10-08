preco = float(input('Digite o preço do produto: '))

desconto = (preco*0.05)
print('O novo preço do produto com 5% de desconto é R${:.2f}'.format(preco - desconto))