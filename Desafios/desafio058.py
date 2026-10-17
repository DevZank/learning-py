# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

import random

num = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10])
numUser = int(input('Escolha um número de 0 a 10: '))

while numUser != num:
        if numUser > 10 or numUser < 0:
            print('Valor fora do intervalo!')
        else:
            print('Você Errou! Tente novamente!')
        numUser = int(input('Escolha um número de 0 a 10: '))

print(f'Você Acertou! O número era {num}')