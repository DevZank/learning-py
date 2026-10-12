# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último = Souza

nomeCompleto = input('Digite seu nome completo: ')
nomeSplit = nomeCompleto.split()
length = len(nomeSplit)
print('Primeiro nome: {}'.format(nomeSplit[0]))
print('Último nome: {}'.format(nomeSplit[length-1]))