"""
	Analisa se 3 seguimentos de reta podem formar um triângulo
	Adição de condições para classificar os triângulos.
"""

reta1 = int(input('Digite o primeiro seguimento de reta: '))
reta2 = int(input('Digite o segundo seguimento de reta: '))
reta3 = int(input('Digite o terceiro seguimento de reta: '))

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
	print('É POSSÍVEL montar um triângulo com esses seguimentos de reta.')
	if reta1 == reta2 == reta3:
		print('Será formado um triâgulo equilátero.')
	elif reta3 != reta2 != reta1 != reta3:
		print('Será formado um triâgulo escaleno.')
	else:
		print('Será formado um triâgulo Isósceles.')
else:
	print('Tamanho das retas INSUFICIENTE para formar um triângulo.')
