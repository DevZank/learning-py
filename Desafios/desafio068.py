# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

v = 0

while True:
    jOpt = input('Par ou Ímpar [P/I]? ').strip().upper()
    jNum = int(input('Digite um número: '))

    mNum = randint(0, 100)

    if jOpt == 'P' and (mNum + jNum) % 2 == 0:
        v += 1
        print(f'Você ganhou! A soma dos valores {jNum} + {mNum} = {jNum + mNum}')
    elif jOpt == 'I' and (mNum + jNum) % 2 != 0:
        v += 1
        print(f'Você ganhou! A soma dos valores {jNum} + {mNum} = {jNum + mNum}')
    else:
        print(f'Você perdeu! A soma dos valores {jNum} + {mNum} = {jNum + mNum}')
        break
print(f'Vitórias consecutivas: {v}!')