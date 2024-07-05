from datetime import date
sexo = ''

try:
    sexo = str(input('Digite o sexo [M/F]: '))
except ValueError:
    print('Digite M - Para sexo masculino, e F - Para sexo feminino.')

if sexo.upper() != 'F':
    try:
        ano_nascimento = int(input('Ano de nascimento: '))
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento
        print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')

        if idade == 18:
            print(f'Você precisa se alistar este ano PRA VIRAR PÉ PRETO!')
        elif idade < 18:
            print(f'Você deverá se alistar em {ano_nascimento + 18} ainda'
                  f' {"faltam" if 18 - idade > 1 else "falta"} {18 - idade}'  # Inclusão de IF ternário
                  f' {"anos" if 18 - idade > 1 else "ano"}.')                 # (IF linha)
        else:
            print(f'Você deveria ter se alistado em {ano_nascimento + 18}')
    except ValueError:
        print('Digite o valor do ano no formato numérico de 4 dígitos!')
else:
    print('Você não precisa se alistar!')
