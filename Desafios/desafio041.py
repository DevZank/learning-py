# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Em que ano você Nasceu? '))
idade = anoAtual - anoNasc

if idade <= 9:
    print('Você está na Categoria MIRIM com {} anos'.format(idade))
elif idade <= 14:
    print('Você está na Categoria INFANTIL com {} anos'.format(idade))
elif idade <= 19:
    print('Você está na Categoria JÚNIOR com {} anos'.format(idade))
elif idade <= 25:
    print('Você está na Categoria SÊNIOR com {} anos'.format(idade))
elif idade > 25:
    print('Você está na Categoria MASTER com {} anos'.format(idade))