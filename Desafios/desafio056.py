# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nome = input('Qual o nome? ')
idade = int(input('Qual a idade? '))
sexo = input('Qual o sexo [F | M]? ')

mediaIdade = idade
nomeMaisVelho = ''
idadeMaisVelho = 0
qntMenos20 = 0

if sexo.upper() == 'M':
    nomeMaisVelho = nome
    idadeMaisVelho = idade

if sexo.upper() == 'F' and idade < 20:
    qntMenos20 += 1

for c in range(3):
    nome = input('Qual o nome? ')
    idade = int(input('Qual a idade? '))
    sexo = input('Qual o sexo [F | M]? ')

    mediaIdade += idade

    if sexo.upper() == 'M' and idadeMaisVelho < idade:
        nomeMaisVelho = nome
        idadeMaisVelho = idade

    if sexo.upper() == 'F' and idade < 20:
        qntMenos20 += 1

mediaIdade = mediaIdade / 4

print('\nA média de idades é {} anos'.format(mediaIdade))
print('O Homem mais velho é {}'.format(nomeMaisVelho))
print('A quantidade de mulheres com menos de 20 é {}'.format(qntMenos20))