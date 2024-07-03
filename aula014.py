# for c in range(0, 10):
#     print(c)
# print('Fim.\n')

c = 0
while c < 10:
    print(c)
    c += 1
print('Fim \n')

print('#' * 30)
numero = 1
while numero != 0:
    numero = int(input('Digite um valor: '))
print('Outro Fim! \n')

print('#' * 30)
num = 0
resposta = 'S'
while resposta.upper() == 'S':
    num = int(input('Digite um valor: '))
    resposta = input('Deseja continuar? [S/N] ')
print('Agora é Fim mesmo.')
print('Outro Fim! \n')

print('#' * 30)
num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} impares.')
print('Não, realmente, AGORA acabou!')
