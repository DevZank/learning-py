# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c and c == a:
        print('O Triângulo é EQUILÁTERO!')
    elif a != b and b != c and c != a:
        print('O Triângulo é ESCALENO!')
    elif a == b or b == c or c == a:
        print('O Triângulo é ISÓSCELES!')
else:
    print('O valor das retas não podem formar um triângulo!')
