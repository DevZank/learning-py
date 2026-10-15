#  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase_original = input('Digite uma frase: ')

palavra_sem_espacos = frase_original.split()
palavra_sem_espacos = ''.join(palavra_sem_espacos)

quantidade_letras = len(palavra_sem_espacos.strip())

indice_original = 0

frase_invertida = ''
frase_normal = ''

for indice_reverso in range(quantidade_letras, 0, -1):

    caractere_invertido = palavra_sem_espacos[indice_reverso - 1]
    caractere_normal = palavra_sem_espacos[indice_original]

    indice_original += 1

    frase_invertida += caractere_invertido
    frase_normal += caractere_normal

if frase_invertida == frase_normal:
    print('A frase {} é um palíndromo!'.format(frase_original))
else:
    print('A frase {} não é um palíndromo!'.format(frase_original))