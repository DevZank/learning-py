# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

n = input('Digite o nome do Produto: ').strip()
p = float(input('Digite o preço do Produto: R$').strip())

a = p
b = 0

if p > 1000:
    b += 1

cPrice = p
cName = n

while True:
    br = input('Deseja continuar [S/N]? ').strip().upper()[0]

    if br == 'N':
        break

    n = input('Digite o nome do Produto: ').strip().upper()
    p = float(input('Digite o preço do Produto: R$').strip())

    a += p

    if p > 1000:
        b += 1

    if p < cPrice:
        cPrice = p
        cName = n

print(f'O gasto total foi R${a}')
print(f'{b} produtos custaram mais de R$1.000')
print(f'O produto mais barato foi {cName}')