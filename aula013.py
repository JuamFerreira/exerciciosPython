numero = int(input('Digite um valor: '))

for c in range(0, numero+1):
    print(c)
print('Fim.\n')

inicio = int(input('Digite o número de início: '))
fim = int(input('Digite o número final: '))
intervalo = int(input('Digite o intervalo da contagem: '))

for d in range(inicio, fim+1, intervalo):
    print(d)
print('Outro Fim.\n')

soma = 0
for c in range(0, 3):
    num = int(input('Digite um valor: '))
    soma += num
print(f'A soma dos valores é: {soma}')
print('Fim real!')
