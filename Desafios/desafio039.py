# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Em que ano você Nasceu? '))
idade = anoAtual - anoNasc

if idade > 18:
    print('Já se passaram {} anos do tempo de se alistar para o Serviço Militar!'.format(idade - 18))
elif idade < 18:
    print('Você ainda vai precisar se alistar! Em {} anos!'.format(18 - idade))
else:
    print('Está na hora de se ALISTAR!')