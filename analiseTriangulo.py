""" Analisa se 3 seguimentos de reta podem formar um triângulo """

reta1 = int(input('Digite o primeiro seguimento de reta: '))
reta2 = int(input('Digite o segundo seguimento de reta: '))
reta3 = int(input('Digite o terceiro seguimento de reta: '))

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
	print('É POSSÍVEL montar um triângulo com esses seguimentos de reta.')
else:
	print('Tamanho das retas INSUFICIENTE para formar um triângulo.')
