# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite seu salário: '))
aumento = 0

if sal > 1250.00:
    aumento = 0.1
else:
    aumento = 0.15

newSal = sal + sal * aumento

print('Seu novo salário com aumento é R${}'.format(newSal))