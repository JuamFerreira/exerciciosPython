"""
    Elabora a tabuada de um número fornecido pelo usuário.
"""

numero = int(input('Digite o numerador: '))
for den in range(1, 11):
    print(f'{numero} x {den} = {numero * den}')
