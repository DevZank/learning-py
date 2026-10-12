frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 14))
print(frase.find('deo')) # Em qual index encontro o começo de 'deo'
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '   Aprendenda Python  '
print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())

frase = 'Curso em Vídeo Python'
fraseCortado = frase.split()
print(fraseCortado)
print('|'.join(fraseCortado))