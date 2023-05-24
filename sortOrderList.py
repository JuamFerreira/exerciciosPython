from random import shuffle

ordem = []
for i in range(4):
	ordem.append(input('Digite o nome para a lista: '))

shuffle(ordem)
print('A nova ordem de apresentação será \n', ordem)
