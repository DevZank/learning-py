#  Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. ]
#  Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

num = int(input('Digite um número: '))
f1 = 0
f2 = 1
tot = 1
i = 0

while i < num:
    print(f1, end=' ')
    tot += f1
    f1 = f2
    f2 = tot
    i += 1