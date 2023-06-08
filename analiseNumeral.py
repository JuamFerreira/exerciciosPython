""" Analisa as posições de um numeral e retorna sua classe """

numero = int(input('Digite um numeral com até 6 algarismos: '))

print(f'{" "*6}Analisando o numeral {numero}')

if len(str(numero)) <= 6:
    print(f'Unidade:            {numero // 1 % 10}')
    print(f'Dezena:             {numero // 10 % 10}')
    print(f'Centena:            {numero // 100 % 10}')
    print(f'Unidade de Milhar:  {numero // 1000 % 10}')
    print(f'Dezena de Milhar:   {numero // 10000 % 10}')
    print(f'Centena de Milhar:  {numero // 100000 % 10}')
else:
    print("Número fora do tamanho esperado.")
