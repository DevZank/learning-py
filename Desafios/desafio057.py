# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite o sexo [M/F]: ')
while sexo.upper() != 'M' and sexo.upper() != 'F':
    sexo = input('INVALIDO! Digite o sexo [M/F]: ')
print(f'FIM! O sexo digitado foi {sexo.upper()}')