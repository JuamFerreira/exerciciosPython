from random import choice

alunos = []

for i in range(4):
	alunos.append(input(f'Digite o nome do alune {i+1}: '))

print(choice(alunos), 'foi a alune escolhide!')
