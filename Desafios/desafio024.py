# Crie um programa que leia o nome de uma cidade e diga
# se ela começa ou não com o nome "SANTO"

cidade = input('Digite o nome de uma cidade: ')

cSplit = cidade.split()
startSanto = 'SANTO' in cSplit[0].upper()
print('Contem Santo? {}'.format(startSanto))