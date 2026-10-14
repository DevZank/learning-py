# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))
option = int(input('[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\nEscolha a base de conversão: '))

if option == 1:
    print('O número {} convertido em binário é {}!'.format(num, bin(num)[2:]))
elif option == 2:
    print('O número {} convertido em octal é {}!'.format(num, oct(num)[2:]))
elif option == 3:
    print('O número {} convertido em hexadecimal é {}!'.format(num, hex(num)[2:]))
else:
    print('Opção não Encontrada!')