# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
import math

# Ex: Digite um número: 6.127
# O número 6.127 tem a parte
# Inteira 6.

n = float(input('Digite um número: '))

print('A Parte inteira de {} é {}!'.format(n, (math.floor(n))))