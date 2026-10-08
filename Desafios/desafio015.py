dias = int(input('Informe os dias usados: '))
distancia = float(input('Informe os Km percorridos: '))

preco = (dias * 60) + (distancia * 0.15)

print('O total a pagar é R${:.2f}'.format(preco))