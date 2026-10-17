# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))

i = 0
while i < 10:
    print(t, end=' ')
    t += r
    i += 1