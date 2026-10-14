# Crie um programa que faça o computador jogar Jokenpô com você.

import random

pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
user = input('\n[Pedra]\n[Papel]\n[Tesoura]\nEscolha uma opção: ')

if pc == user:
    print('EMPATE!')
elif pc == 'Pedra' and user == 'Tesoura':
    print('Você perdeu! A maquina escolheu {}'.format(pc))
elif pc == 'Tesoura' and user == 'Pedra':
    print('Você ganhou! A maquina escolheu {}'.format(pc))
elif pc == 'Tesoura' and user == 'Papel':
    print('Você perdeu! A maquina escolheu {}'.format(pc))
elif pc == 'Papel' and user == 'Tesoura':
    print('Você ganhou! A maquina escolheu {}'.format(pc))
elif pc == 'Pedra' and user == 'Papel':
    print('Você ganhou! A maquina escolheu {}'.format(pc))
elif pc == 'Papel' and user == 'Pedra':
    print('Você perdeu! A maquina escolheu {}'.format(pc))