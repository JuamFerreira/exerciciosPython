""" Analisa as posições de um numeral e retorna sua classe """

numero = input('Digite um numeral com 4 algarismos: ')

print(f'{" "*6}Analisando o numeral {numero}')

if len(numero) == 4:
    print(f'Unidade: {numero[3]}')
    print(f'Dezena: {numero[2]}')
    print(f'Centena: {numero[1]}')
    print(f'Unidade de Milhar: {numero[0]}')
else:
    print("Número fora do tamanho esperado.")
