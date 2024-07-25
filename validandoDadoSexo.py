"""
    Programa faz uma validação para aceitar o dado correto para sexo.
"""

sexo = input('Digite seu sexo [M/F]: ').strip()[0]
while sexo not in 'MmFf':
    sexo = input('Dado inválido, Informe o sexo corretamente: ').strip()[0]
nome = input('Digite seu nome: ')
print(f'Bem vind{"a" if sexo in "Ff" else "o"}, {nome}!')
