# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtual = date.today().year

totMenor = 0
totMaior = 0

for c in range(7):
    anoNasc = int(input('Digite o ano de Nascimento: '))
    idade = anoAtual - anoNasc

    if idade >= 18:
        totMaior += 1
    else:
        totMenor += 1

print('Ao total temos {} pessoas de maior e {} de menor!'.format(totMaior, totMenor))