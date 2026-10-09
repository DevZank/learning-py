# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt

cOposto = float(input('Digite o comprimento do cateto oposto: '))
cAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = sqrt((cOposto**2)+(cAdjacente**2))

print('O comprimento da hipotenusa é {:.1f}'.format(hipotenusa))

