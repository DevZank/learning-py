# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano para saber se ele é Bissextos: '))

if ano % 4 == 0:
    print('O Ano {} é BISSEXTO!'.format(ano))
else:
    print('O Ano {} não é BISSEXTO!'.format(ano))