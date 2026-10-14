# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# E R$0,45 para viagens mais longas

dist = float(input('Digite a distancia em Km: '))
preco = 0

if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45

print('O preço da viagem é R${:.0f}'.format(preco))