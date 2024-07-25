"""
    Programa analisa o menor e o maior peso adicionados em uma sequência de valores.
"""

menor = maior = 0
for controle in range(1, 6):
    peso = float(input(f'Digite o {controle}º peso: '))
    if controle == 1:
        menor = maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O menor peso é {menor}Kg, e o maior peso é {maior}Kg.')
