"""
    Programa analisa o nome, idade e sexo de uma sequência de pessoas e retorna algumas informações.
"""

somaIdade = 0
maiorIdadeHomem = 0
maisVelhoHomem = ''
qtdMulherMenor20 = 0

for pessoa in range(1, 5):
    print(f'{"-"*5} {pessoa}º PESSOA {"-"*5}')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()

    somaIdade += idade

    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        maisVelhoHomem = nome
    if idade > maiorIdadeHomem and sexo in 'Mm':
        maiorIdadeHomem = idade
        maisVelhoHomem = nome
    if sexo in 'Ff' and idade < 20:
        qtdMulherMenor20 += 1

mediaIdade = somaIdade / 4

print(f'{"="*7} RESULTADO {"="*7}')

print(f'A média de idade do grupo é {mediaIdade}.')
print(f'O homem mais velho do grupo é {maisVelhoHomem} com {maiorIdadeHomem} anos de idade.')
print(f'Há {qtdMulherMenor20} mulheres menores de 20 anos.')
