# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
ts = int(input('Quantos Termos deseja ver? '))

i = 0

while ts != 0:
    while i < ts:
        print(t, end=' ')
        t += r
        i += 1
    i = 0
    ts = int(input('\nQuantos mais termos deseja ver? '))
print('---FIM---')