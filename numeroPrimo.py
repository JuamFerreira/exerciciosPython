"""
    Identifica se o número informado pelo usuário é primo ou não
"""

contador = 0
numero = int(input('Digite um número: '))
for controle in range(1, numero+1):
    if numero % controle == 0:
        contador += 1
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print(f' {controle}', end=' ')
if contador == 2:
    print(f'\n {numero} É um número primo!')
else:
    print(f'\n \033[m {numero} Não é um número primo pois é divisível por {contador} '
          f'número{"s" if contador > 1 else " apenas"}.')
