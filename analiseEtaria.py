"""
    Analisa um número determinado de idade e classifica quantos estão na maioridade ou não
"""
from datetime import date

maiorIdade = 0
menorIdade = 0

for controle in range(0, 7):
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - nascimento
    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print(f'Há {maiorIdade} pessoas na maior idade, e {menorIdade} pessoas menores de idade.')
