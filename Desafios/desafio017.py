# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

cOposto = float(input('Digite o comprimento do cateto oposto: '))
cAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(cOposto, cAdjacente)

print('O comprimento da hipotenusa é {:.1f}'.format(hipotenusa))

