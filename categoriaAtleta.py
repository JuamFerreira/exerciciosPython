"""
    Informa a categoria do atleta de acordo com sua idade.
"""
from datetime import date

dt_nascimento = int(input('Digite o ano de nascimento (4 digitos): '))
idade = date.today().year - dt_nascimento

if idade <= 9:
    print(f'Com {idade} anos o atleta está na categoria MIRIM.')
elif idade <= 14:
    print(f'Com {idade} anos o atleta está na categoria INFANTIL.')
elif idade <= 19:
    print(f'Com {idade} anos o atleta está na categoria JUNIOR.')
elif idade <= 25:
    print(f'Com {idade} anos o atleta está na categoria SÊNIOR.')
else:
    print(f'Com {idade} anos o atleta está na categoria MASTER.')
