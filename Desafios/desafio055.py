# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = float(input('Digite peso da pessoa em Kg: '))

menor = peso
maior = peso

for c in range(4):
    peso = float(input('Digite peso da pessoa em Kg: '))

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print('O Maior peso foi: {:.1f}Kg, e o menor peso foi: {:.1f}Kg'.format(maior, menor))