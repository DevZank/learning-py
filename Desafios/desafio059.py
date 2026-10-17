# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

control = 0

while control != 5:
    control = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\nSelecione uma Opção: '))

    if control == 1:
        print(f'\nA soma de {n1} + {n2} = {n1+n2}\n')
    elif control == 2:
        print(f'\nA multiplicação {n1} x {n2} = {n1*n2}\n')
    elif control == 3:
        if n1 > n2:
            print(f'\nO maior valor é {n1}\n')
        elif n1 < n2:
            print(f'\nO maior valor é {n2}\n')
        else:
            print(f'\nOs valores são iguais!\n')
    elif control == 4:
        n1 = int(input('\nDigite um número: '))
        n2 = int(input('Digite outro número: '))
print('----FIM----')