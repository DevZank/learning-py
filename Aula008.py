# import biblioteca
# from biblioteca import livro
# from biblioteca import livro, item
# import math - ceil - floor - trunc - pow - sqrt - factorial

from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz arredondado pra cima de {} é igual a {}'.format(num, ceil(raiz)))
print('A raiz arredondado pra baixo de {} é igual a {}'.format(num, floor(raiz)))