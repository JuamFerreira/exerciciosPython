""" Analisa se uma palavra ou frase é um palíndromo """

print('~~~=' * 15)
print('Analise se uma frase ou palavra é um palíndromo')
print('~~~=' * 15)

palindromo = input('Digite sua palavra ou frase: ')
rv_palindromo = palindromo.replace(' ', '')[::-1]

if palindromo.replace(' ', '').lower() == rv_palindromo.lower():
	print(f'{palindromo} - é um palindromo!')
else:
	print(f'{rv_palindromo} é diferente de {palindromo}, por tanto não é um palíndromo.')
