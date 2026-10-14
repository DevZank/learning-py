# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice
# de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura )

if imc < 18.5:
    print('Seu IMC é {:.1f}! ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f}! PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f}! SOBREPESO!'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.1f}! OBESIDADE!'.format(imc))
else:
    print('Seu IMC é {:.1f}! OBESIDADE MÓRBIDA!'.format(imc))