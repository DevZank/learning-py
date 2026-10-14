# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.choice([0, 1, 2, 3, 4, 5])
numUser = int(input('Escolha um número de 0 a 5: '))
if numUser == num:
    print("Você Acertou! O número era {}".format(num))
else:
    print("Você Errou! O número era {}".format(num))
