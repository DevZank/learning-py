# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

a = 0
b = 0
c = 0

while True:
    i = int(input('Digite a idade: ').strip())
    s = input('Digite o sexo [M/F]: ').strip().upper()[0]

    if s == 'F':
        if i < 20:
            c += 1
    elif s == 'M':
        b += 1
    else:
        print('Sexo Inválido!')

    if i > 18:
        a += 1

    br = input('Deseja continuar [S/N]? ').strip().upper()[0]

    if br == 'N':
        break

print(f'\n{a} pessoas tem mais de 18 anos!')
print(f'{b} homens foram cadastrados!')
print(f'{c} mulheres tem menos de 20 anos')