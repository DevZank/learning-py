# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número: '))
startNum = num
fat = 1

while num != 1:
    fat *= num
    num -= 1

print(f'O Fatorial de {startNum} = {fat}')