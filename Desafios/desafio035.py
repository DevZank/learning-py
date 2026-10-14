# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('O valor das retas podem formar um triângulo!')
else:
    print('O valor das retas não podem formar um triângulo!')