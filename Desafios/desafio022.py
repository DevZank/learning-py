# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O Nome com todas as letras letras maiúsculas
# - O Nome com todas as letras letras minúsculas
# - Quantas letras ao todoo (sem considerar espaços).
# - Quantas letras tem o primeiro nome

nomeCompleto = input('Digite seu nome completo: ')

p1 = nomeCompleto.upper()
p2 = nomeCompleto.lower()
p3 = nomeCompleto.split()
p3 = len(''.join(p3))
p4 = nomeCompleto.split()
p4 = len(p4[0])

print('O nome em maiúsculas: {}'.format(p1))
print('O nome em minúsculas: {}'.format(p2))
print('O Nome tem {} letras'.format(p3))
print('O Primeiro Nome tem {} letras'.format(p4))