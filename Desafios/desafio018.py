# Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite um angulo: '))

radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print('O Seno é {:.3f}, O Cosseno é {:.3f}, Tangente é {:.3f}'.format(seno, cosseno, tangente))