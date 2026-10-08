# Para adição +
# Para subtração -
# Para multiplicação *
# Para divisão /
# Para potencia **
# Para divisão inteira //
# Para resto da divisão %
import math

# Ordem de precedência
# 1 | ()
# 2 | **
# 3 | * _ / _ // _ %
# 4 | + _ -

# Forma de calcular raiz quadrada com potencia
# 81**(1/2) - Raiz quadrada
# 81**(1/3) - Raiz cubica

print(math.sqrt(81))
print('='*20)

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n1
di = n1 // n2
e = n1 ** n2

print('A soma é {}, \n o produto é {} e a divisão é {:.3}'.format(s, m, d), end='') # End ' ' não quebra a linha
print('Divisão inteira {} e potência {}'.format(di, e))