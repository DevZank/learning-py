#  Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#  mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

c = 1
r = 'S'
n = int(input('Digite um número: '))
r = input('Deseja continuar [S/N]? ')
min = max = m = n

while r.upper() != 'N':
    n = int(input('Digite um número: '))
    r = input('Deseja continuar [S/N]? ')
    if n > max:
        max = n

    if n < min:
        min = n
    m += n
    c += 1
print(f'A média é {m/c} e o maior valor foi {max} o menor foi {min}!')