nome = input('Qual é seu nome? ')

if nome == 'Isaac':
    print('Que nome bacana!')
elif nome == 'Guilherme' or nome == 'Maria' or nome == 'Gabriel':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Mario Jonathan Rodrigo':
    print('Um bom nome!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))