"""
    Um jogo onde a máquina sorteia um ítem de uma lista e confere com a escolha do usuário.
"""
from random import randint
from time import sleep

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
maquina = randint(0, 2)

print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
try:
    usuario = int(input('Faça sua escolha: '))
except ValueError:
    print('Valor Inválido! Escolha um número das opções acima.')
else:
    if usuario in range(0, 3):
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!')
        sleep(1)

        print('=-' * 12)
        print(f'Você jogou {opcoes[usuario]}')
        print(f'A máquina jogou {opcoes[maquina]}')

        if usuario == maquina:
            print('empate')
        else:
            if usuario == 0:  # Pedra
                if maquina == 2:  # Tesoura
                    print('VOCÊ GANHOU!')
                else:                     # A única possibilidade restante é Papel
                    print('Você perdeu')
            elif usuario == 1:
                if maquina == 0:
                    print('VOCÊ GANHOU!')
                else:
                    print('Você perdeu')
            elif usuario == 2:
                if maquina == 1:
                    print('VOCÊ GANHOU!')
                else:
                    print('Você perdeu')
        print('-=' * 12)
    else:
        print('Valor Inválido! Escolha um número das opções acima.')
