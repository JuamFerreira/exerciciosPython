"""
    Realiza uma contagem regressiva
"""

from time import sleep

for cont in range(10, 0, -1):
    print(cont)
    sleep(1)
print('BOOM POU POU rondondondondoom')

"""
    Contagem de 2 a 2
"""
for num in range(2, 51, 2):
    print(num, end=' ')
print('')

"""
    Soma múltiplos de 3 num intervalo
"""
soma = 0
contador = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero
        contador += 1
print(f'A soma de todos os {contador} números impares múltiplos de 3 entre 1 e 500 é {soma}.')
