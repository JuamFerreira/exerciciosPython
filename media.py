"""
    Programa calcula a média de 2 notas de 1 aluno
"""

nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
media = (nota1 + nota2) / 2

print(f'A média entre {nota1} e {nota2} é {media}')

if media >= 7:
    print(f'O aluno está Aprovado')
elif media < 5:
    print('Aluno Reprovado!')
else:
    print('Aluno de recuperação!')
