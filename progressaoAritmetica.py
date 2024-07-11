"""
    Cria uma PA com os dados informados pelo usuário
"""

pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
dt = pt + (10 - 1) * razao
for numero in range(pt, dt+razao, razao):
    print(numero, end=' <- ')
