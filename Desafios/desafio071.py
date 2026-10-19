# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

vSaque = int(input('Qual valor será sacado? R$'))

n50 = n20 = n10 = n1 = 0

while True:
    if vSaque >= 50:
        n50 += 1
        vSaque -= 50
    elif vSaque >= 20:
        n20 += 1
        vSaque -= 20
    elif vSaque >= 10:
        n10 += 1
        vSaque -= 10
    elif vSaque >= 1:
        n1 += 1
        vSaque -= 1
    else:
        break

print(f'Você recebe {n50} nota de R$50')
print(f'Você recebe {n20} nota de R$20')
print(f'Você recebe {n10} nota de R$10')
print(f'Você recebe {n1} nota de R$1')