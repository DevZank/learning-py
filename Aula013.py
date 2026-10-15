for c in range(6, 0, -2):
    print(c)
print('FIM')

for c in range(0, 7, 2):
    print(c)
print('FIM')

for c in range(0, 6):
    print('Oi')
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um numero: '))
    s += n
print('A soma de todos os números foi: {}'.format(s))
