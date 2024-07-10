"""
    Realiza uma contagem regressiva
"""

from time import sleep

for cont in range(10, 0, -1):
    print(cont)
    sleep(1)
print('BOOM POU POU rondondondondoom')

for num in range(0, 51, 2):
    print(num, end=' ')
