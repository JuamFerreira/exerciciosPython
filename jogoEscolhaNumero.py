from random import randint
from time import sleep

# Jogada da máquina
maquina = randint(0, 5)
print('~~¬' * 10)
print('escolhendo um número de 0 a 5')
print('~~¬' * 10)

# jogada do usuário
user = int(input('Adivinhe o número escolhido: '))
print('\nPROCESSANDO...')
sleep(3)

# Processamento e resposta
if maquina == user:
	print('PARABÉNS, VOCÊ GANHOU!')
else:
	print(f'Você perdeu, a máquina escolheu o número {maquina}')
