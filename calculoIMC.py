"""
    Calcula o IMC de uma pessoa baseado em sua altura e peso.
"""

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

if altura.is_integer():
    """ ajusta o valor da altura se passado como inteiro """
    altura = altura / 100

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC {imc:.2f} ---- Abaixo do peso')
elif imc <= 25.0:
    print(f'IMC {imc:.2f} ---- Peso ideal')
elif imc <= 30.0:
    print(f'IMC {imc:.2f} ---- Sobrepeso')
elif imc <= 40.0:
    print(f'IMC {imc:.2f} ---- Obesidade')
else:
    print(f'IMC {imc:.2f} ---- Obesidade mórbida')
