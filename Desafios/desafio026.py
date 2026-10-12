# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')

countA = frase.upper().count('A')
findStartA = frase.upper().find('A')
findEndA = frase.upper().rfind('A')

print('A frase contém a letra A, {} vezes'.format(countA))
print('Aparece na posição {} pela primeira vez'.format(findStartA))
print('Aparece na posição {} pela última vez'.format(findEndA))