""" Converte um valor para outra base numérica """

valor = int(input('Digite um valor inteiro: '))
print('''Digite a opção de acordo com qual base numérica deseja converter:
      [ 1 ] Para Binário
      [ 2 ] Para Octal
      [ 3 ] Para Hexadecimal''')
opção = int(input('Digite a opção: '))


if opção == 1:
	print(f'{valor} convertido para binário é: { bin(valor)[2:] }')
elif opção == 2:
	print(f'{valor} convertido para octal é: {oct(valor)[2:]}')
elif opção == 3:
	print(f'{valor} convertido para hexadecimal é: {hex(valor)[2:]}')
else:
	print('Opção inválida!')
